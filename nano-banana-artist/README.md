# Nano Banana Artist

Create stunning images with natural language using Google's Gemini 3.1 Flash Image model — right inside Claude Code.

> Built by [Vistoso.ai](https://vistoso.ai)

## Quick Start

1. Install the plugin:
   ```bash
   /plugin marketplace add The-Edgar/vistoso-ai-skills
   /plugin install nano-banana-artist@vistoso-ai-skills
   ```

2. Get a free Gemini API key at https://aistudio.google.com/apikey

3. Save it:
   ```bash
   echo 'your-key' > ~/.gemini_api_key
   chmod 600 ~/.gemini_api_key
   ```

4. Ask Claude to create an image — the skill activates automatically.

## Features

- **Photorealistic photography** — portraits, products, food, landscapes
- **Logo & text rendering** — state-of-the-art text accuracy in generated images
- **Delta editing** — precise single-change iterations on existing images
- **Character consistency** — named characters stay consistent across generations
- **Resolution control** — 512 / 1K / 2K / 4K via `--image-size`
- **Flexible aspect ratios** — 1:1, 16:9, 9:16, 4:5, 3:2, 21:9, and more
- **Up to 14 reference images** — for style matching and character consistency

## Usage Examples

Just talk to Claude naturally:

- "Create a professional headshot of a woman in a modern office"
- "Design a logo for my coffee shop called 'Bean There'"
- "Make a product photo of these sneakers on a marble surface"
- "Edit this image — change the background to a sunset"

## License

MIT — see [LICENSE](../LICENSE)
