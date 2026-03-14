# TTS Worker (OpenAI + R2, KV metadata-only)

This Cloudflare Worker provides secure TTS generation without exposing API keys in frontend.

## Architecture

- **KV (`TTS_CACHE`)** stores metadata only (`meta:<hash>`)
- **R2 (`AUDIO_BUCKET`)** stores audio binary (`audio/<hash>.mp3`)
- Frontend calls `POST /tts`, then plays `audio_url` (and optional `audio_base64` for immediate first playback)

## Features

- On-demand generation (no request, no cost)
- Shared cache by content hash
- Same text + params generated once and reused
- Cache-first read path (metadata KV -> audio from R2)
- No GitHub repo persistence job required

## API

### `POST /tts`

Body:

```json
{
  "text": "你好，世界",
  "lang": "zh",
  "provider": "openai",
  "voice_id": "alloy",
  "format": "mp3"
}
```

Response:

```json
{
  "audio_url": "https://your-worker-domain/audio/<hash>",
  "audio_base64": "...",
  "cache_hit": true
}
```

### `GET /audio/<hash>`

Returns audio bytes from R2.

## Deploy

1. Install Wrangler
2. Configure `wrangler.toml` (copy from `wrangler.toml.example`)
3. Create R2 bucket (once):

```bash
wrangler r2 bucket create external-brain-tts-audio
```

4. Set secret:

```bash
wrangler secret put OPENAI_API_KEY
```

5. Deploy:

```bash
wrangler deploy
```

## Frontend config

Set in `index.html` before script execution:

```html
<script>
  window.TTS_API_ENDPOINT = "https://your-worker-domain/tts";
  window.OPENAI_TTS_VOICE = "alloy";
</script>
```

If `window.TTS_API_ENDPOINT` is empty, frontend falls back to browser `speechSynthesis`.
