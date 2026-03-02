# Prompt Templates for Nano Banana 2 (Gemini 3.1 Flash Image)

Complete library of proven prompt templates using structured production-grade prompting.

## The 7-Element Formula

Every template follows the same structure — use what applies, skip what doesn't:

```
Subject + Action + Setting + Style + Camera + Lighting + Constraints
```

Simple requests use 3 elements. Complex requests use all 7. No mode switching needed.

## Advanced Techniques

### Variable Definitions for Complex Compositions
When creating multi-element images, define variables to keep attributes distinct:

```
OBJECT_A = red sports car, OBJECT_B = blue mountain bike, LIGHTING_C = golden hour sunlight.
Show OBJECT_A and OBJECT_B side by side with LIGHTING_C creating long shadows.
```

**Why it works**: Prevents attribute mixing, maintains spatial and stylistic coherence.

### Search Grounding for Factual Imagery
Gemini 3.1 can verify facts using Google Search for accurate representations:

```
Generate a scientifically accurate diagram of the James Webb Space Telescope with labeled components
```

**Use cases**: Scientific diagrams, architectural landmarks, historical accuracy, current events

### Reference Image Composition
Supports up to 14 reference images via `--image`:
- Up to 6 object images for consistent props/items
- Up to 5 human images for character consistency
- Maintains visual fidelity across multi-turn conversations

## Photorealistic Photography Templates

### Portrait Photography
```
[Subject name], [expression], [action/pose].
[Setting], [time of day]. [Camera lens] at [aperture], [angle].
[Lighting], [mood]. [Constraints].
```

**Example:**
```
Elena, warm smile, adjusting her glasses thoughtfully.
Modern glass office with city views, golden hour. 85mm at f/1.8, eye level.
Soft window light, professional yet approachable. No text.
```

### Landscape Photography
```
[Location with geographic features], [time of day], [weather].
[Foreground elements], [background elements].
[Camera lens] at [aperture], [angle]. [Lighting], [mood].
[Constraints].
```

**Example:**
```
Misty mountain valley with pine forest, sunrise, fog-filled.
Wildflowers in foreground, snow-capped peaks behind.
24mm at f/11, wide angle. Soft golden light breaking through mist, serene.
16:9. No people.
```

### Action/Sports Photography
```
[Subject] performing [specific action] at peak moment.
[Motion elements: spray, dust, debris]. [Setting].
[Fast shutter], [camera settings], [angle].
[Lighting]. [Constraints].
```

**Example:**
```
Surfer carving a wave at the lip, spray exploding behind.
Turquoise water, late afternoon. 1/2000s, 200mm telephoto, low angle from water.
Golden backlight through spray. No text.
```

### Product Photography
```
[Product description] on [surface material and color].
[Lighting setup], [angle], [key feature to showcase].
[Format]. [Constraints].
```

**Example:**
```
Matte black wireless headphones on dark walnut surface.
Three-point softbox, 45-degree angle, textured ear cushion detail.
1:1. No text, no props.
```

### Food Photography
```
[Dish name and key ingredients] plated on [plate description].
[Plating style]. [Lighting], [angle].
[Texture details to capture]. [Constraints].
```

**Example:**
```
Pan-seared salmon with asparagus and lemon butter, white ceramic plate.
Modern plating, microgreens garnish. Soft window light from left, overhead angle.
Capture steam, glisten on sauce, crispy skin texture. No text.
```

### Fashion/Clothing Photography
```
[Clothing item] worn by [model description].
[Setting], [lighting setup]. [Camera angle and lens].
Emphasize [fabric texture, fit, color]. [Mood]. [Constraints].
```

**Example:**
```
Oversized camel wool coat worn by tall woman with short dark hair.
Minimalist concrete studio, soft diffused overhead light. Full body, 50mm.
Emphasize drape and texture of wool. Editorial, confident. No text.
```

## Logo and Brand Design Templates

**Note**: Gemini 3.1 Flash Image excels at text rendering with state-of-the-art accuracy.

### Minimalist Logo
```
Logo for [company], a [type of business].
Text "[exact text]", [font style]. [Symbol/icon]. [Color scheme].
Scalable, works in color and monochrome. [Constraints].
```

**Example:**
```
Logo for TechFlow, a cloud computing startup.
Text "TechFlow", clean sans-serif. Flowing arrow symbol. Navy and cyan gradient.
Scalable, works in color and monochrome. No tagline.
```

### Wordmark Logo
```
Wordmark logo for "[Brand Name]".
[Font style] conveying [brand personality].
[Design elements: ligatures, custom characters]. [Color scheme].
Clean, legible at all sizes. [Constraints].
```

### Logo with Icon
```
Logo combining icon and text for [company], a [industry].
Icon: [style] representation of [concept], [position relative to text].
Text "[Company Name]" in [font style]. [Color palette].
Icon works independently as favicon. [Constraints].
```

## Sticker and Icon Design Templates

### Character Sticker
```
[Style: kawaii/cute/bold] sticker of [character with personality traits].
[Expressive elements: large eyes, specific pose]. [Outline style].
[Color palette]. White background. Die-cut ready.
```

**Example:**
```
Kawaii sticker of a sleepy owl holding a coffee cup.
Half-closed eyes, steam swirls. Bold clean outlines, cel-shaded.
Warm brown and cream palette. White background. Die-cut ready.
```

### Icon Set
```
Set of [number] [style: flat/line/glyph] icons for [theme/category].
[Size], [stroke weight]. Unified visual language.
[Color]. Pixel-aligned, scalable. [Constraints].
```

## Delta Editing Templates

All editing follows the delta pattern: state what stays, state what changes, front-load constraints.

### Single Element Change
```
Do not [constraint]. Do not [constraint].
Keep [element A], [element B], and [element C] unchanged.
Change only [target element] from [current state] to [new state].
```

**Example:**
```
Do not add text. Do not change the person's expression.
Keep pose, clothing, and lighting unchanged.
Change only the background from office interior to rooftop terrace at sunset.
```

### Color/Material Swap
```
Keep everything else exactly the same, including lighting and shadows.
Change only the [specific element] from [current material/color] to [new material/color].
New [material/color] should react naturally to existing light sources.
```

**Example:**
```
Keep everything else exactly the same, including lighting and shadows.
Change only the wall color from white to sage green.
New color should react naturally to existing window light, showing appropriate highlights.
```

### Style Transfer
```
Transform into the style of [artist/movement/period].
Preserve original composition and subject placement.
Render with [characteristic techniques: brushwork, palette, stylistic elements].
[Constraints].
```

**Example:**
```
Transform into the style of impressionist painting.
Preserve original composition and subject placement.
Render with visible brushwork, vibrant complementary colors, and soft edges.
No text overlay.
```

### Layout Lock (Reframe Without Moving Subject)
```
Subject stays centered at current scale.
Replace only the background with [new background description].
Match lighting direction and color temperature to new setting.
[Constraints].
```

**Example:**
```
Subject stays centered at current scale.
Replace only the background with a neon-lit Tokyo street at night.
Match lighting direction — key light from front-left stays. Add subtle neon color spill.
No text. No additional people.
```

### Object Addition
```
Keep all existing elements unchanged.
Add [detailed object description] at [specific location with spatial reference].
New object should match existing [lighting, shadows, perspective].
[Constraints].
```

**Example:**
```
Keep all existing elements unchanged.
Add a small succulent in a white ceramic pot to the right side of the desk, next to the laptop.
New plant should match soft window light from left, casting subtle shadow to the right.
No text.
```

### Object Removal
```
Remove [specific object] from [location].
Reconstruct background by matching surrounding [textures, patterns, colors].
No trace of removed object. [Constraints].
```

## Creative Director Templates (Platform-Agnostic)

Describe PURPOSE and FORMAT, never platform names.

### Professional Headshot
```
[Subject name], approachable expression, confident posture.
Studio lighting, neutral background. 1:1, sharp focus.
No text. No distracting elements.
```

**Example:**
```
Dr. Amara, approachable smile, professional posture.
Soft studio lighting, light grey background. 1:1, sharp.
No text. No props.
```

### Product Listing Hero
```
[Product] on clean white background, studio lit.
[Angle], soft shadow. 1:1.
No props, no text, no background clutter.
```

**Example:**
```
Leather messenger bag on clean white background, studio lit.
45-degree angle, soft drop shadow. 1:1.
No props, no text. Show stitching and brass hardware detail.
```

### Vertical Short-Form Frame
```
[Subject] mid-action, vibrant.
9:16, saturated colors. Bold, high energy.
[Constraints].
```

**Example:**
```
Barista pouring latte art, mid-pour, vibrant.
9:16, warm saturated tones. Bold, inviting energy.
No text. Shallow DOF on cup.
```

### Widescreen Hero Image
```
[Subject/scene], cinematic composition.
16:9, [mood]. [Lighting].
[Constraints].
```

**Example:**
```
Mountain trail at golden hour, solo hiker silhouette.
16:9, adventurous and aspirational. Warm backlight, dramatic sky.
No text. No logos.
```

### Editorial Feature
```
[Subject] in [environment], editorial quality.
[Aspect ratio], [lighting], [camera].
[Mood]. [Constraints].
```

## Specialized Templates

### Comic Book Panel
```
Single comic panel in [art style: manga, superhero, BD].
[Character] [action] showing [emotional state].
Background: [setting with mood]. [Camera angle].
[Speech/caption]: "[exact text]". [Lighting].
```

### Architectural Visualization
```
[Building type and style] featuring [key architectural elements].
[Context: urban, landscape], [time of day].
[Materials: glass, concrete, wood]. [Camera angle and lens].
[Design philosophy]. [Constraints].
```

### Interior Design Mockup
```
[Style] interior of [room type] with [key furniture].
[Natural and artificial lighting]. [Color scheme].
[Mood]. [Format]. [Constraints].
```

### Before/After Split Screen
```
Split-screen comparison of [subject].
Left: [before state]. Right: [after state].
Consistent lighting, identical camera angle. Labels "Before" and "After" in [font].
```

### Sequential Storytelling
```
[Number]-panel sequence: [narrative].
Panel 1: [scene]. Panel 2: [scene]. [Continue...]
Consistent art style and character appearance. [Color palette].
```

## Technical Specifications

### Size Selection
Use `--image-size` flag — keep resolution out of prompts:
- **512** — Quick drafts, thumbnails
- **1K** (DEFAULT) — Standard digital use
- **2K** — Professional work
- **4K** — Print production

### Aspect Ratio Selection
- **1:1** — Square feed, profile pictures, universal
- **4:5** — Tall feed format, maximum mobile visibility
- **16:9** — Widescreen hero, presentations, headers
- **9:16** — Vertical short-form, mobile-first
- **3:2** — Photography standard, print
- **21:9** — Cinematic, ultra-wide

### Resolution Guide
- **Digital feed**: 1K at target aspect ratio
- **Web headers/heroes**: 2K at 16:9
- **Print**: 4K, 300 DPI minimum, CMYK color space
- **Quick iteration**: 1K, then re-generate final at target size

## Prompt Enhancement Patterns

### Adding Depth
```
[Close foreground element]. [Main subject in middle ground].
[Background context], slightly out of focus for depth.
```

### Enhancing Realism
```
With realistic [material behavior: fabric wrinkling, liquid motion, light refraction].
[Environmental interaction: wind effect, steam rising, cast shadows].
```

### Controlling Mood
```
[Primary mood] atmosphere.
[Lighting quality], [color temperature], [environmental effects: mist, particles, haze].
```

## Common Modifications

### "Make it pop"
Add: "High contrast, saturated colors, dramatic lighting, clear focal point"

### "Professional look"
Add: "Clean composition, balanced elements, subtle palette, professional lighting"

### "Modern aesthetic"
Add: "Minimalist, geometric shapes, contemporary palette, clean lines, negative space"

### "Warm and inviting"
Add: "Warm color temperature, soft lighting, golden hour tones, welcoming composition"
