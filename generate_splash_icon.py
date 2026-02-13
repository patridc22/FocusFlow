#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

def create_clean_icon(size, filename):
    # Create white background
    img = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(img)

    # Draw simple gradient circle in center
    center = size // 2
    radius = int(size * 0.35)

    # Create gradient effect with concentric circles
    for i in range(radius, 0, -2):
        # Purple to lighter purple gradient
        ratio = i / radius
        r = int(102 + (200 - 102) * (1 - ratio))
        g = int(126 + (180 - 126) * (1 - ratio))
        b = int(234 + (255 - 234) * (1 - ratio))

        draw.ellipse([center - i, center - i, center + i, center + i],
                    fill=(r, g, b))

    # Try to load a font for "FF" text
    try:
        # Try to use a system font
        font_size = int(size * 0.35)
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/Library/Fonts/Arial.ttf", int(size * 0.35))
        except:
            # Fallback to default font
            font = ImageFont.load_default()

    # Draw "FF" in white in the center
    text = "FF"

    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center the text
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - int(size * 0.02)

    draw.text((x, y), text, fill='white', font=font)

    # Save
    img.save(filename, 'PNG')
    print(f'Created {filename}')

# Generate all required sizes
create_clean_icon(512, '/Users/patri/FocusFlow/icon-512.png')
create_clean_icon(192, '/Users/patri/FocusFlow/icon-192.png')
create_clean_icon(180, '/Users/patri/FocusFlow/apple-touch-icon.png')

print('✅ Clean splash icons generated!')
