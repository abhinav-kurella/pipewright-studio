# Diwali 2026: how this was made

## 1. Scene (generated in ChatGPT image generation)
```
Photorealistic vertical photo, 4:5 ratio. A warm, elegant home office on Diwali evening. A sleek silver all-in-one desktop computer (iMac style) sits on a dark walnut desk. Its screen shows a minimal dark analytics dashboard with four rising bars, the tallest bar golden with a tiny glowing diya flame on top.

On the deep terracotta wall above the desk: 3D brushed-brass letters reading "Pipewright Studio", mounted on small stand-offs, casting soft realistic shadows on the wall. Beneath it, a small brass plaque engraved "Abhinav Kumar".

Diwali details: a string of warm fairy lights across the top of the wall, three small lit clay diyas on the desk, scattered marigold petals, a copper desk lamp glowing softly. Cinematic warm lighting, shallow depth of field, premium and minimal, natural reflections on the screen glass. Leave clean empty wall space in the top quarter for a headline. No other text, no watermark.
```

**For brand-consistent signage, describe the letters as:** "3D brushed-brass serif letters in a classic Baskerville style, bold weight".

## 2. Brand layer (added afterwards)
- Label: "HAPPY DIWALI", IBM Plex Mono, letter-spaced, brass
- Headline: "Bright homes. / Brighter pipelines.", Libre Baskerville Bold (brand display font, matches the wall sign)
- Logo: brass Pipewright mark added left of the AI-generated wall sign (from brand/logo)
- Status only: "Wishing you a Diwali full of light, and a year full of good conversations.", IBM Plex Sans
- Status size: wall extended below the fairy lights to reach 9:16, with nothing cropped

## Files
| File | Use |
|---|---|
| `scene-original.png` | Raw generated scene, 1122×1402 |
| `diwali-post-1080x1350.png` | Instagram feed, LinkedIn, WhatsApp chats |
| `diwali-status-1080x1920.png` | WhatsApp status, Instagram story |

## Editable source
- `source/poster.html` + `source/scene.png` / `scene-tall.png`: open `poster.html?w=1080&h=1350` (post) or `?w=1080&h=1920` (status) in a browser, or screenshot with Playwright, to change the headline and re-export.
- `alternates/`: two earlier code-drawn versions (rangoli, pipeline drawing) with their HTML sources.
- Versions built on Adobe Stock photos are not stored here: the raw stock files are licensed to Abhinav's Adobe account and shouldn't be redistributed in a public repo.
