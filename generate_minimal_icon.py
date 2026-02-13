#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

def create_minimal_icon(size, filename):
    # Create image with solid gradient background
    img = Image.new('RGB', (size, size))
    draw = ImageDraw.Draw(img)

    # Draw smooth gradient (purple)
    for y in range(size):
        # Gradient from #667eea to #764ba2
        ratio = y / size
        r = int(102 + (118 - 102) * ratio)
        g = int(126 + (75 - 126) * ratio)
        b = int(234 + (162 - 234) * ratio)
        draw.rectangle([(0, y), (size, y+1)], fill=(r, g, b))

    # Draw simple ".c" letter in center
    try:
        # Use system font
        font_size = int(size * 0.45)
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/SFNSDisplay.ttf", int(size * 0.45))
        except:
            try:
                font = ImageFont.truetype("/Library/Fonts/Arial.ttf", int(size * 0.45))
            except:
                font = ImageFont.load_default()

    # Draw ".c" in white
    text = ".c"

    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center the text
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - int(size * 0.03)

    # Draw with slight shadow for depth
    shadow_offset = max(2, size // 100)
    draw.text((x + shadow_offset, y + shadow_offset), text, fill=(0, 0, 0, 30), font=font)
    draw.text((x, y), text, fill='white', font=font)

    # Add subtle rounded corners effect
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    corner_radius = int(size * 0.22)  # iOS-style rounded corners
    mask_draw.rounded_rectangle([(0, 0), (size, size)], corner_radius, fill=255)

    # Apply mask
    img.putalpha(mask)

    # Save
    img.save(filename, 'PNG')
    print(f'Created {filename}')

# Generate all required sizes
create_minimal_icon(512, '/Users/patri/FocusFlow/icon-512.png')
create_minimal_icon(192, '/Users/patri/FocusFlow/icon-192.png')
create_minimal_icon(180, '/Users/patri/FocusFlow/apple-touch-icon.png')

print('✅ Minimal elegant icons generated!')
