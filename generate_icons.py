#!/usr/bin/env python3
"""Generate PNG icons for iOS PWA support"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, filename):
    """Create a Serbian flag-inspired icon with Cyrillic letter"""
    # Create image with rounded corners
    img = Image.new('RGB', (size, size), color='#667eea')
    draw = ImageDraw.Draw(img)

    # Draw Serbian tricolor stripes (simplified)
    stripe_height = size // 6
    # Red stripe
    draw.rectangle([0, size//2 - stripe_height, size, size//2], fill='#c41e3a')
    # Blue stripe
    draw.rectangle([0, size//2, size, size//2 + stripe_height], fill='#0056b3')

    # Try to add text (Cyrillic Ћ or fallback to icon emoji)
    try:
        # Try to use a large font for the emoji
        font_size = int(size * 0.5)
        # Use default font as fallback
        # Draw white circle background for better contrast
        circle_size = int(size * 0.65)
        circle_x = (size - circle_size) // 2
        circle_y = (size - circle_size) // 2
        draw.ellipse([circle_x, circle_y, circle_x + circle_size, circle_y + circle_size],
                     fill='white', outline='#667eea', width=max(2, size//50))

        # Draw Cyrillic letter Ћ in the center
        font_size = int(size * 0.45)
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            font = ImageFont.load_default()

        text = "Ћ"
        # Get text bounding box for centering
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (size - text_width) // 2 - bbox[0]
        y = (size - text_height) // 2 - bbox[1]

        draw.text((x, y), text, fill='#667eea', font=font)

    except Exception as e:
        print(f"Text rendering failed: {e}, using simple design")

    # Save with high quality
    img.save(filename, 'PNG', quality=95, optimize=True)
    print(f"Created {filename} ({size}x{size})")

# Create icons for iOS
create_icon(180, 'icon-180.png')  # iPhone Retina
create_icon(192, 'icon-192.png')  # Manifest requirement
create_icon(512, 'icon-512.png')  # Manifest requirement

print("\nIcons generated successfully!")
print("Note: For production, consider creating custom icons with a design tool.")
