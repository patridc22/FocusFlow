#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

def create_text_splash(width, height, filename):
    # Create white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", int(height * 0.08))
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", int(height * 0.04))
    except:
        try:
            title_font = ImageFont.truetype("/Library/Fonts/Arial.ttf", int(height * 0.08))
            subtitle_font = ImageFont.truetype("/Library/Fonts/Arial.ttf", int(height * 0.04))
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()

    # Text
    title = ".complete"
    subtitle = "your tasks & focus"

    # Get text sizes
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]

    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_height = subtitle_bbox[3] - subtitle_bbox[1]

    # Center positions
    title_x = (width - title_width) // 2
    title_y = (height - title_height - subtitle_height - 20) // 2

    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = title_y + title_height + 20

    # Draw text
    draw.text((title_x, title_y), title, fill='#667eea', font=title_font)
    draw.text((subtitle_x, subtitle_y), subtitle, fill='#999999', font=subtitle_font)

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
