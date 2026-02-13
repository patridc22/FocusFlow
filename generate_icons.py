#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

def create_icon(size, filename):
    # Create image with gradient background
    img = Image.new('RGB', (size, size))
    draw = ImageDraw.Draw(img)

    # Draw gradient (purple to blue)
    for y in range(size):
        r = int(102 + (118 - 102) * y / size)
        g = int(126 + (75 - 126) * y / size)
        b = int(234 + (162 - 234) * y / size)
        draw.rectangle([(0, y), (size, y+1)], fill=(r, g, b))

    # Draw target circles
    center = size // 2
    colors_opacity = [(255, 255, 255, 80), (255, 255, 255, 130), (255, 255, 255, 180)]
    radii = [int(size * 0.35), int(size * 0.27), int(size * 0.2)]

    # Create new image with alpha for circles
    overlay = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)

    for radius, color in zip(radii, colors_opacity):
        draw_overlay.ellipse([center - radius, center - radius, center + radius, center + radius],
                           outline=color, width=max(2, size//64))

    # Convert base image to RGBA and paste overlay
    img = img.convert('RGBA')
    img = Image.alpha_composite(img, overlay)

    # Draw center dot (target)
    dot_radius = int(size * 0.12)
    draw = ImageDraw.Draw(img)
    draw.ellipse([center - dot_radius, center - dot_radius, center + dot_radius, center + dot_radius],
                fill=(255, 107, 107))

    # Draw arrow
    arrow_width = max(2, size // 32)
    arrow_length = int(size * 0.55)
    arrow_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    arrow_draw = ImageDraw.Draw(arrow_img)

    # Arrow shaft
    arrow_draw.rectangle([center - arrow_width, center - arrow_length//2,
                         center + arrow_width, center + arrow_length//2],
                        fill=(255, 217, 61))

    # Arrow head
    head_size = int(size * 0.08)
    arrow_draw.polygon([(center, center - arrow_length//2 - head_size),
                       (center - head_size, center - arrow_length//2 + head_size),
                       (center + head_size, center - arrow_length//2 + head_size)],
                      fill=(255, 217, 61))

    # Arrow tail
    tail_size = int(size * 0.03)
    arrow_draw.polygon([(center, center + arrow_length//2 + tail_size),
                       (center - tail_size, center + arrow_length//2),
                       (center + tail_size, center + arrow_length//2)],
                      fill=(255, 217, 61))

    # Rotate arrow
    arrow_img = arrow_img.rotate(-45, expand=False)

    # Composite arrow onto main image
    img = Image.alpha_composite(img, arrow_img)

    # Save
    img.save(filename, 'PNG')
    print(f'Created {filename}')

# Generate all required sizes
create_icon(512, '/Users/patri/FocusFlow/icon-512.png')
create_icon(192, '/Users/patri/FocusFlow/icon-192.png')
create_icon(180, '/Users/patri/FocusFlow/apple-touch-icon.png')
create_icon(32, '/Users/patri/FocusFlow/favicon.png')

print('✅ All icons generated!')
