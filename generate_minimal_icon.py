#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

def create_minimal_icon(size, filename):
    # Create RGBA image for transparency support
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Modern flat design - solid purple background
    # Using a clean, modern purple (#667eea)
    corner_radius = int(size * 0.225)  # iOS-style rounded corners
    draw.rounded_rectangle([(0, 0), (size, size)], corner_radius, fill='#667eea')

    # Modern, clean font - larger, bolder
    try:
        # Try SF Pro or Helvetica for clean modern look
        font_size = int(size * 0.50)
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/Library/Fonts/Arial.ttf", int(size * 0.50))
        except:
            font = ImageFont.load_default()

    # Simple ".c" text
    text = ".c"

    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center the text perfectly
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - int(size * 0.02)

    # Draw text - NO SHADOW, clean and flat
    draw.text((x, y), text, fill='white', font=font)

    # Save with transparency
    img.save(filename, 'PNG')
    print(f'Created {filename}')

# Generate all required sizes
create_minimal_icon(512, '/Users/patri/FocusFlow/icon-512.png')
create_minimal_icon(192, '/Users/patri/FocusFlow/icon-192.png')
create_minimal_icon(180, '/Users/patri/FocusFlow/apple-touch-icon.png')

print('✅ Minimal elegant icons generated!')
