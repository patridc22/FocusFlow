#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

# Create a simple screenshot with just text
img = Image.new('RGB', (540, 720), 'white')
draw = ImageDraw.Draw(img)

# Load font
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 50)
except:
    try:
        font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 50)
    except:
        font = ImageFont.load_default()

# Text
text = ".complete"
subtitle = "your tasks."

# Get text sizes and center
bbox1 = draw.textbbox((0, 0), text, font=font)
bbox2 = draw.textbbox((0, 0), subtitle, font=font)

text_width1 = bbox1[2] - bbox1[0]
text_width2 = bbox2[2] - bbox2[0]

x1 = (540 - text_width1) // 2
x2 = (540 - text_width2) // 2
y1 = 300
y2 = 360

# Draw text
draw.text((x1, y1), text, fill='#667eea', font=font)
draw.text((x2, y2), subtitle, fill='#667eea', font=font)

# Save
img.save('/Users/patri/FocusFlow/screenshot.png', 'PNG')
print('✅ Screenshot created')
