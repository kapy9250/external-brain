# TTS Worker (OpenAI default, cache-first)

This Cloudflare Worker provides secure TTS generation without exposing API keys in frontend.

Default provider is OpenAI TTS (`provider: "openai"`). ElevenLabs remains optional.

## Features

- On-demand generation (no request, no cost)
- Shared cache by content hash
- Same text + params generated once and reused
- Cache-first read path (KV first)
- Periodic persistence from KV to GitHub repo (`audio-cache/*.mp3`) via cron

## API

`POST /tts`

Body:

```json
{
  "text": "你好，世界",
  "lang": "zh",
  "voice_id": "agczkAUlHLowaNnL72Cc",
  "format": "mp3_44100_128"
}
```

Response:

```json
{
  "audio_url": "https://your-cdn-domain/audio/abcd1234.mp3",
  "audio_base64": "...",
  "cache_hit": true
}
```

Manual persistence trigger (optional):

`POST /persist`

## Deploy

1. Install Wrangler
2. Configure `wrangler.toml` (see `wrangler.toml.example`)
3. Set secrets:

```bash
wrangler secret put OPENAI_API_KEY
wrangler secret put GH_PAT
```

> `GH_PAT` needs repo write permission to persist `audio-cache/*.mp3`.

4. Deploy:

```bash
wrangler deploy
```

## Frontend config

Set in `index.html` before script execution:

```html
<script>
  window.TTS_API_ENDPOINT = "https://your-worker-domain/tts";
  window.ELEVENLABS_VOICE_ID = "agczkAUlHLowaNnL72Cc";
</script>
```

If `window.TTS_API_ENDPOINT` is empty, frontend falls back to browser `speechSynthesis`.
