#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

def create_text_splash(width, height, filename):
    # Create white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    # Load font - clean, simple
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", int(height * 0.055))
    except:
        try:
            font = ImageFont.truetype("/Library/Fonts/Arial.ttf", int(height * 0.055))
        except:
            font = ImageFont.load_default()

    # Simple text
    text = ".complete your tasks."

    # Get text size
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center position
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Draw text - simple, clean color
    draw.text((x, y), text, fill='#667eea', font=font)

    # Save
    img.save(filename, 'PNG')
    print(f'Created {filename}')

# Common iOS device sizes
splash_sizes = [
    (1125, 2436, 'splash-1125x2436.png'),  # iPhone X, XS, 11 Pro
    (1242, 2688, 'splash-1242x2688.png'),  # iPhone XS Max, 11 Pro Max
    (828, 1792, 'splash-828x1792.png'),    # iPhone XR, 11
    (1170, 2532, 'splash-1170x2532.png'),  # iPhone 12, 12 Pro, 13, 13 Pro
    (1284, 2778, 'splash-1284x2778.png'),  # iPhone 12 Pro Max, 13 Pro Max
    (1179, 2556, 'splash-1179x2556.png'),  # iPhone 14, 14 Pro, 15
    (1290, 2796, 'splash-1290x2796.png'),  # iPhone 14 Pro Max, 15 Pro Max
    (750, 1334, 'splash-750x1334.png'),    # iPhone 8, SE
    (1125, 2436, 'splash-1125x2436.png'),  # iPhone X
]

for width, height, filename in splash_sizes:
    create_text_splash(width, height, f'/Users/patri/FocusFlow/{filename}')

print('✅ All text-only splash screens generated!')
