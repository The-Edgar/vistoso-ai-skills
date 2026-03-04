#!/usr/bin/env python3
"""
Gemini Image Generation Script (Nano Banana 2)
Calls Google's Gemini 3.1 Flash Image API to generate high-quality images.
Supports --image-size control (512/1K/2K/4K) for resolution selection.
"""

import os
import sys
import json
import base64
import argparse
from pathlib import Path

def get_api_key():
    """
    Get API key from multiple possible sources.
    Priority: 1) Environment variable, 2) ~/.gemini_api_key file
    """
    # Method 1: Environment variable
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key:
        return api_key

    # Method 2: User home directory config file
    home_key_path = os.path.expanduser('~/.gemini_api_key')
    if os.path.exists(home_key_path):
        with open(home_key_path, 'r') as f:
            api_key = f.read().strip()
            if api_key:
                return api_key

    # No key found
    print("Error: GEMINI_API_KEY not found", file=sys.stderr)
    print("\nPlease set your API key using ONE of these methods:", file=sys.stderr)
    print("  1. Environment variable: export GEMINI_API_KEY='your-key'", file=sys.stderr)
    print("  2. Home config file:     echo 'your-key' > ~/.gemini_api_key && chmod 600 ~/.gemini_api_key", file=sys.stderr)
    print("\nGet your free API key at: https://aistudio.google.com/apikey", file=sys.stderr)
    print("Need help? Email help@vistoso.ai", file=sys.stderr)
    sys.exit(1)

def call_gemini_api(prompt, aspect_ratio="1:1", output_path="generated_image.png",
                    image_paths=None, response_modalities=None, image_size="1K"):
    """
    Call Gemini 3.1 Flash Image API to generate high-quality images.

    Args:
        prompt: Text prompt for image generation
        aspect_ratio: Image aspect ratio (1:1, 16:9, 9:16, etc.)
        output_path: Where to save the generated image
        image_paths: Optional list of input images for editing (up to 14 images supported)
        response_modalities: Optional list like ['Image'] or ['Text', 'Image']
        image_size: Output image size - '512', '1K', '2K', or '4K' (default: '1K')
    """

    # Get API key from multiple possible sources
    api_key = get_api_key()

    # Build the request payload
    contents = []

    # Add input images if provided (for editing)
    if image_paths:
        # Ensure image_paths is a list
        if not isinstance(image_paths, list):
            image_paths = [image_paths]

        # Add all images to the parts array
        parts = []
        for image_path in image_paths:
            with open(image_path, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')

            # Determine mime type
            ext = Path(image_path).suffix.lower()
            mime_types = {
                '.png': 'image/png',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.webp': 'image/webp'
            }
            mime_type = mime_types.get(ext, 'image/png')

            parts.append({
                "inline_data": {
                    "mime_type": mime_type,
                    "data": image_data
                }
            })

        contents.append({"parts": parts})

    # Add text prompt
    if not contents:
        contents.append({"parts": [{"text": prompt}]})
    else:
        contents[0]["parts"].append({"text": prompt})
    
    # Build generation config
    # Map image_size to ImageSize parameter
    size_map = {
        '512': '512',
        '1K': '1024',
        '2K': '2048',
        '4K': '4096',
    }
    output_image_size = size_map.get(image_size, '1024')

    generation_config = {
        "imageConfig": {
            "aspectRatio": aspect_ratio,
            "ImageSize": output_image_size,
        }
    }
    
    if response_modalities:
        generation_config["responseModalities"] = response_modalities
    
    payload = {
        "contents": contents,
        "generationConfig": generation_config
    }
    
    # Make the API call using curl (to avoid dependencies)
    import subprocess

    curl_cmd = [
        'curl', '-s', '-X', 'POST',
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent',
        '-H', f'x-goog-api-key: {api_key}',
        '-H', 'Content-Type: application/json',
        '-d', '@-'  # Read JSON from stdin
    ]

    try:
        # Pass payload via stdin to avoid "Argument list too long" error with large images
        result = subprocess.run(curl_cmd, input=json.dumps(payload), capture_output=True, text=True, check=True)
        response_data = json.loads(result.stdout)
        
        # Extract image data from response
        if 'candidates' in response_data and len(response_data['candidates']) > 0:
            parts = response_data['candidates'][0]['content']['parts']
            
            # Find the image part
            for part in parts:
                if 'inlineData' in part:
                    image_b64 = part['inlineData']['data']
                    
                    # Decode and save
                    image_bytes = base64.b64decode(image_b64)
                    with open(output_path, 'wb') as f:
                        f.write(image_bytes)
                    
                    print(f"✅ Image saved to: {output_path}")
                    return output_path
                elif 'text' in part:
                    # Print any text response
                    print(f"Response: {part['text']}")
            
            print("Warning: No image found in response", file=sys.stderr)
            return None
        else:
            print(f"Error: {response_data}", file=sys.stderr)
            return None
            
    except subprocess.CalledProcessError as e:
        print(f"API call failed: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Generate high-quality images using Google Gemini 3.1 Flash Image API (Nano Banana 2)'
    )
    parser.add_argument('prompt', help='Text prompt for image generation')
    parser.add_argument('--aspect-ratio', default='1:1',
                       choices=['1:1', '1:2', '1:3', '1:4', '1:8', '2:3', '3:2', '3:4', '4:3', '4:5', '5:4', '9:16', '16:9', '21:9'],
                       help='Image aspect ratio (default: 1:1)')
    parser.add_argument('--image-size', default='1K',
                       choices=['512', '1K', '2K', '4K'],
                       help='Output image size (default: 1K)')
    parser.add_argument('--output', '-o', default='generated_image.png',
                       help='Output file path (default: generated_image.png)')
    parser.add_argument('--image', '-i', action='append', dest='images',
                       help='Input image(s) for editing (can be specified multiple times, up to 14 images)')
    parser.add_argument('--image-only', action='store_true',
                       help='Return only image, no text (uses responseModalities)')

    args = parser.parse_args()

    response_modalities = ['Image'] if args.image_only else None

    call_gemini_api(
        prompt=args.prompt,
        aspect_ratio=args.aspect_ratio,
        output_path=args.output,
        image_paths=args.images,
        response_modalities=response_modalities,
        image_size=args.image_size
    )

if __name__ == '__main__':
    main()
