# TTS Worker (ElevenLabs, cache-first)

This Cloudflare Worker provides secure TTS generation without exposing API keys in frontend.

## Features

- On-demand generation (no request, no cost)
- Shared cache by content hash
- Same text + params generated once and reused
- Frontend only gets `audio_url`

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
  "cache_hit": true
}
```

## Deploy

1. Install Wrangler
2. Configure `wrangler.toml` (see `wrangler.toml.example`)
3. Set secret:

```bash
wrangler secret put ELEVENLABS_API_KEY
```

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
