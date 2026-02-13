#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

def create_minimal_icon(size, filename):
    # Create RGBA image for transparency support
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Elegant black background - timeless, classy
    corner_radius = int(size * 0.225)  # iOS-style rounded corners
    draw.rounded_rectangle([(0, 0), (size, size)], corner_radius, fill='#1a1a1a')

    # Much smaller, refined font - with lots of whitespace
    try:
        font_size = int(size * 0.28)  # Reduced from 0.48 to 0.28
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/Library/Fonts/Arial.ttf", int(size * 0.28))
        except:
            font = ImageFont.load_default()

    # Elegant ".c" text - smaller and more subtle
    text = ".c"

    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center the text perfectly
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - int(size * 0.02)

    # Draw text in elegant off-white
    draw.text((x, y), text, fill='#f5f5f5', font=font)

    # Save with transparency
    img.save(filename, 'PNG')
    print(f'Created {filename}')

# Generate all required sizes
create_minimal_icon(512, '/Users/patri/FocusFlow/icon-512.png')
create_minimal_icon(192, '/Users/patri/FocusFlow/icon-192.png')
create_minimal_icon(180, '/Users/patri/FocusFlow/apple-touch-icon.png')

print('✅ Minimal elegant icons generated!')
