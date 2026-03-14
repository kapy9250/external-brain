export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders(env, request) });
    }

    if (request.method === 'POST' && url.pathname === '/tts') {
      return handleTTS(request, env);
    }

    if (request.method === 'GET' && url.pathname.startsWith('/audio/')) {
      return handleAudio(url.pathname.replace('/audio/', ''), env, request);
    }

    // legacy endpoint retained for compatibility
    if (request.method === 'POST' && url.pathname === '/persist') {
      return json({ ok: true, skipped: true, reason: 'R2 mode: no repo persistence task' }, 200, env, request);
    }

    return json({ error: 'Not found' }, 404, env, request);
  },

  async scheduled(_event, _env, _ctx) {
    // no-op in R2 mode
  }
};

async function handleTTS(request, env) {
  try {
    const { text = '', lang = 'zh', voice_id = '', format = 'mp3', provider = 'openai' } = await request.json();
    const normalized = normalizeText(text);
    if (!normalized) return json({ error: 'text is required' }, 400, env, request);

    const ttsVoice = (voice_id || env.OPENAI_TTS_VOICE || 'alloy');
    const ttsModel = env.OPENAI_TTS_MODEL || 'gpt-4o-mini-tts';

    const hash = await sha256Hex(`${provider}|${ttsVoice}|${lang}|${format}|${normalized}`);
    const metaKey = `meta:${hash}`;

    const existing = await env.TTS_CACHE.get(metaKey, 'json');
    if (existing?.audio_path) {
      return json({
        audio_url: `${originFromRequest(request)}/audio/${hash}`,
        audio_base64: null,
        cache_hit: true
      }, 200, env, request);
    }

    // Simple lock via KV (best-effort)
    const lockKey = `lock:${hash}`;
    const lock = await env.TTS_CACHE.get(lockKey);
    if (lock) {
      // Wait briefly for concurrent request to finish
      await sleep(600);
      const retryMeta = await env.TTS_CACHE.get(metaKey, 'json');
      if (retryMeta?.audio_path) {
        return json({ audio_url: `${originFromRequest(request)}/audio/${hash}`, cache_hit: true }, 200, env, request);
      }
    }
    await env.TTS_CACHE.put(lockKey, '1', { expirationTtl: 60 });

    let ttsRes;

    if (provider === 'openai') {
      ttsRes = await fetch('https://api.openai.com/v1/audio/speech', {
        method: 'POST',
        headers: {
          'authorization': `Bearer ${env.OPENAI_API_KEY}`,
          'content-type': 'application/json'
        },
        body: JSON.stringify({
          model: ttsModel,
          voice: ttsVoice,
          input: normalized,
          format: format || 'mp3'
        })
      });
    } else {
      ttsRes = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${ttsVoice}`, {
        method: 'POST',
        headers: {
          'xi-api-key': env.ELEVENLABS_API_KEY,
          'content-type': 'application/json',
          'accept': 'audio/mpeg'
        },
        body: JSON.stringify({
          text: normalized,
          model_id: 'eleven_multilingual_v2',
          output_format: 'mp3_44100_128',
          voice_settings: {
            stability: 0.45,
            similarity_boost: 0.8,
            style: 0.35,
            use_speaker_boost: true
          }
        })
      });
    }

    if (!ttsRes.ok) {
      const errText = await ttsRes.text();
      await env.TTS_CACHE.delete(lockKey);
      return json({ error: `${provider}_tts_failed`, detail: errText }, 502, env, request);
    }

    const audioBuffer = await ttsRes.arrayBuffer();
    const base64 = arrayBufferToBase64(audioBuffer);

    // Store audio body in R2 (binary), metadata in KV only
    const r2Key = `audio/${hash}.mp3`;
    await env.AUDIO_BUCKET.put(r2Key, audioBuffer, {
      httpMetadata: {
        contentType: 'audio/mpeg',
        cacheControl: 'public, max-age=31536000, immutable'
      }
    });

    await env.TTS_CACHE.put(metaKey, JSON.stringify({
      audio_path: `/audio/${hash}`,
      r2_key: r2Key,
      created_at: Date.now()
    }), { expirationTtl: 60 * 60 * 24 * 30 });

    await env.TTS_CACHE.delete(lockKey);

    return json({
      audio_url: `${originFromRequest(request)}/audio/${hash}`,
      audio_base64: base64,
      cache_hit: false
    }, 200, env, request);
  } catch (e) {
    return json({ error: 'internal_error', detail: String(e) }, 500, env, request);
  }
}

async function handleAudio(hash, env, request) {
  if (!hash) return new Response('Not found', { status: 404, headers: corsHeaders(env, request) });

  const r2Key = `audio/${hash}.mp3`;
  const obj = await env.AUDIO_BUCKET.get(r2Key);
  if (!obj) return new Response('Not found', { status: 404, headers: corsHeaders(env, request) });

  const headers = new Headers(corsHeaders(env, request));
  headers.set('content-type', obj.httpMetadata?.contentType || 'audio/mpeg');
  headers.set('cache-control', obj.httpMetadata?.cacheControl || 'public, max-age=31536000, immutable');

  return new Response(obj.body, {
    status: 200,
    headers
  });
}

function normalizeText(input) {
  return (input || '').replace(/\s+/g, ' ').trim();
}

function json(payload, status, env, request = null) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: {
      ...corsHeaders(env, request),
      'content-type': 'application/json; charset=utf-8'
    }
  });
}

function corsHeaders(env, request = null) {
  const raw = (env.ALLOWED_ORIGIN || '*').trim();

  let allowOrigin = '*';
  if (raw !== '*') {
    const allowList = raw.split(',').map(s => s.trim()).filter(Boolean);
    const reqOrigin = request?.headers?.get('origin') || '';
    if (allowList.includes(reqOrigin)) {
      allowOrigin = reqOrigin;
    } else {
      allowOrigin = allowList[0] || '*';
    }
  }

  return {
    'access-control-allow-origin': allowOrigin,
    'access-control-allow-methods': 'GET,POST,OPTIONS',
    'access-control-allow-headers': 'content-type'
  };
}

function originFromRequest(request) {
  const u = new URL(request.url);
  return `${u.protocol}//${u.host}`;
}

async function sha256Hex(input) {
  const encoder = new TextEncoder();
  const data = encoder.encode(input);
  const hash = await crypto.subtle.digest('SHA-256', data);
  return [...new Uint8Array(hash)].map(b => b.toString(16).padStart(2, '0')).join('');
}

function arrayBufferToBase64(buffer) {
  let binary = '';
  const bytes = new Uint8Array(buffer);
  const chunkSize = 0x8000;
  for (let i = 0; i < bytes.length; i += chunkSize) {
    const chunk = bytes.subarray(i, i + chunkSize);
    binary += String.fromCharCode(...chunk);
  }
  return btoa(binary);
}

function base64ToUint8Array(base64) {
  const binary = atob(base64);
  const len = binary.length;
  const bytes = new Uint8Array(len);
  for (let i = 0; i < len; i++) bytes[i] = binary.charCodeAt(i);
  return bytes;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
