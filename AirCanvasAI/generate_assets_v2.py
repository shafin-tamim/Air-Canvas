from PIL import Image, ImageDraw, ImageFont
import os
import math

# Color Palette
BG_DARK = (18, 18, 28)
BG_DARKER = (12, 12, 20)
ACCENT_CYAN = (0, 188, 212)
ACCENT_PURPLE = (156, 39, 176)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)

# ------------------------
# Create Folders
# ------------------------

folders = [
    "assets/colors",
    "assets/icons",
    "assets/gestures",
    "assets/ui",
    "assets/logo"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# ------------------------
# Colors - Modern Swatch Design
# ------------------------

colors = {
    "red": (255, 59, 48),
    "green": (52, 199, 89),
    "blue": (0, 122, 255),
    "yellow": (255, 204, 0),
    "purple": (175, 82, 222),
    "white": (255, 255, 255)
}

for name, color in colors.items():
    img = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer glow effect
    draw.rounded_rectangle((2, 2, 118, 118), radius=18, fill=(*color, 80), width=0)
    
    # Main color
    draw.rounded_rectangle((8, 8, 112, 112), radius=16, fill=color, width=0)
    
    # Highlight
    draw.ellipse((15, 15, 45, 35), fill=(*WHITE, 150), width=0)
    
    img.save(f"assets/colors/{name}.png")

# ------------------------
# Professional Icons - Modern Design
# ------------------------

def create_icon(name, draw_func):
    img = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background circle with gradient effect
    draw.ellipse((20, 20, 236, 236), fill=(*ACCENT_PURPLE, 40), width=0)
    draw.ellipse((25, 25, 231, 231), fill=(*ACCENT_CYAN, 30), width=0)
    
    # Main background
    draw.ellipse((30, 30, 226, 226), fill=BG_DARK, width=0)
    
    # Border
    draw.ellipse((30, 30, 226, 226), outline=ACCENT_CYAN, width=3)
    
    # Draw the icon symbol
    draw_func(draw, 128, 128)
    
    img.save(f"assets/icons/{name}.png")

def brush_icon(draw, cx, cy):
    # Brush bristles
    draw.polygon([(cx-20, cy-40), (cx-15, cy-15), (cx-25, cy-5), (cx-35, cy-20)], 
                 fill=LIGHT_GRAY)
    draw.polygon([(cx+20, cy-40), (cx+15, cy-15), (cx+25, cy-5), (cx+35, cy-20)], 
                 fill=LIGHT_GRAY)
    draw.polygon([(cx-10, cy-45), (cx+10, cy-45), (cx+5, cy-10), (cx-5, cy-10)], 
                 fill=LIGHT_GRAY)
    # Handle
    draw.rectangle((cx-8, cy-5, cx+8, cy+35), fill=ACCENT_CYAN, width=0)

def eraser_icon(draw, cx, cy):
    # Eraser block
    draw.rectangle((cx-25, cy-30, cx+25, cy+20), fill=(255, 200, 100), width=0)
    draw.rectangle((cx-25, cy-30, cx+25, cy+20), outline=WHITE, width=2)
    # Handle
    draw.rectangle((cx-10, cy+20, cx+10, cy+40), fill=ACCENT_CYAN, width=0)

def save_icon(draw, cx, cy):
    # Floppy disk outline
    draw.rectangle((cx-28, cy-28, cx+28, cy+28), fill=BG_DARKER, outline=WHITE, width=2)
    # Slot
    draw.rectangle((cx-20, cy-28, cx+20, cy-12), fill=ACCENT_CYAN, width=0)
    # Save area
    draw.rectangle((cx-20, cy-8, cx+20, cy+20), fill=ACCENT_CYAN, width=0)

def clear_icon(draw, cx, cy):
    # Trash can
    draw.polygon([(cx-20, cy-25), (cx+20, cy-25), (cx+22, cy-10), (cx-22, cy-10)], 
                 fill=WHITE, width=0)
    draw.rectangle((cx-18, cy-8, cx+18, cy+25), fill=WHITE, outline=WHITE, width=2)
    # Lines in trash
    for i in range(3):
        draw.line([(cx-10+i*10, cy-5), (cx-10+i*10, cy+20)], fill=BG_DARK, width=2)

def undo_icon(draw, cx, cy):
    # Curved arrow
    draw.arc((cx-20, cy-25, cx+20, cy+5), 0, 180, fill=WHITE, width=4)
    draw.polygon([(cx+20, cy+5), (cx+15, cy-5), (cx+28, cy+8)], fill=WHITE)

def redo_icon(draw, cx, cy):
    # Curved arrow (mirrored)
    draw.arc((cx-20, cy-25, cx+20, cy+5), 0, 180, fill=WHITE, width=4)
    draw.polygon([(cx-20, cy+5), (cx-15, cy-5), (cx-28, cy+8)], fill=WHITE)

def settings_icon(draw, cx, cy):
    # Gear
    draw.ellipse((cx-18, cy-18, cx+18, cy+18), fill=WHITE, width=0)
    draw.ellipse((cx-10, cy-10, cx+10, cy+10), fill=BG_DARK, width=0)
    # Teeth
    for angle in range(0, 360, 45):
        x = cx + 25 * math.cos(math.radians(angle))
        y = cy + 25 * math.sin(math.radians(angle))
        draw.rectangle((x-4, y-4, x+4, y+4), fill=WHITE)

def camera_icon(draw, cx, cy):
    # Camera body
    draw.rounded_rectangle((cx-28, cy-20, cx+28, cy+25), radius=5, 
                          fill=BG_DARKER, outline=WHITE, width=2)
    # Lens
    draw.ellipse((cx-15, cy-10, cx+15, cy+15), fill=ACCENT_CYAN, outline=WHITE, width=2)
    # Lens center
    draw.ellipse((cx-8, cy-3, cx+8, cy+8), fill=BG_DARK)

def ai_icon(draw, cx, cy):
    # Neural network nodes
    nodes = [(cx-15, cy-15), (cx+15, cy-15), (cx, cy+10), (cx-15, cy+20), (cx+15, cy+20)]
    for node in nodes:
        draw.ellipse((node[0]-6, node[1]-6, node[0]+6, node[1]+6), 
                    fill=ACCENT_CYAN, outline=WHITE, width=2)
    # Connections
    draw.line([nodes[0], nodes[2]], fill=ACCENT_CYAN, width=2)
    draw.line([nodes[1], nodes[2]], fill=ACCENT_CYAN, width=2)
    draw.line([nodes[2], nodes[3]], fill=ACCENT_CYAN, width=2)
    draw.line([nodes[2], nodes[4]], fill=ACCENT_CYAN, width=2)

icons_map = {
    "brush": brush_icon,
    "eraser": eraser_icon,
    "save": save_icon,
    "clear": clear_icon,
    "undo": undo_icon,
    "redo": redo_icon,
    "settings": settings_icon,
    "camera": camera_icon,
    "ai": ai_icon
}

for icon_name, draw_func in icons_map.items():
    create_icon(icon_name, draw_func)

# ------------------------
# Gesture Cards - Modern Design
# ------------------------

gesture_info = {
    "draw": ("Draw", (100, 255, 200)),
    "move": ("Move", (100, 200, 255)),
    "erase": ("Erase", (255, 150, 100)),
    "finger_gun": ("Gun", (255, 200, 100)),
    "fist": ("Fist", (200, 100, 255)),
    "thumb_up": ("Thumb", (100, 200, 100))
}

for gesture_key, (label, color) in gesture_info.items():
    img = Image.new("RGB", (512, 512), BG_DARK)
    draw = ImageDraw.Draw(img)
    
    # Gradient-like background
    draw.rectangle((20, 20, 492, 492), fill=BG_DARK, outline=0)
    
    # Decorative top bar with color
    draw.rectangle((20, 20, 492, 120), fill=(*color, 100), outline=0)
    draw.rectangle((20, 20, 492, 120), outline=ACCENT_CYAN, width=3)
    
    # Main card area
    draw.rounded_rectangle((20, 20, 492, 492), radius=30, 
                          outline=ACCENT_CYAN, width=4, fill=0)
    
    # Label text
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (512 - text_width) // 2
    text_y = (512 - text_height) // 2
    
    draw.text((text_x, text_y), label, fill=color, font=font)
    
    img.save(f"assets/gestures/{gesture_key}.png")

# ------------------------
# Sidebar - Modern Design
# ------------------------

sidebar = Image.new("RGB", (300, 1080), BG_DARK)
draw = ImageDraw.Draw(sidebar)

# Header with gradient
draw.rectangle((0, 0, 300, 100), fill=BG_DARKER)
draw.rectangle((0, 80, 300, 100), fill=ACCENT_CYAN, width=0)

try:
    font_title = ImageFont.truetype("arial.ttf", 32)
except:
    font_title = ImageFont.load_default()

draw.text((40, 30), "✎ TOOLS", fill=ACCENT_CYAN, font=font_title)

# Divider lines
for y in range(120, 1080, 140):
    draw.line([(20, y), (280, y)], fill=ACCENT_CYAN, width=2)

sidebar.save("assets/ui/sidebar.png")

# ------------------------
# Topbar - Modern Design
# ------------------------

topbar = Image.new("RGB", (1920, 100), BG_DARKER)
draw = ImageDraw.Draw(topbar)

# Header bar
draw.rectangle((0, 0, 1920, 100), fill=BG_DARKER, outline=0)
draw.rectangle((0, 95, 1920, 100), fill=ACCENT_CYAN, width=0)

try:
    font_top = ImageFont.truetype("arial.ttf", 28)
except:
    font_top = ImageFont.load_default()

draw.text((30, 25), "🎨 Air Canvas AI", fill=ACCENT_CYAN, font=font_top)

topbar.save("assets/ui/topbar.png")

# ------------------------
# Splash Screen - Modern Design
# ------------------------

splash = Image.new("RGB", (1920, 1080), BG_DARK)
draw = ImageDraw.Draw(splash)

# Background gradient simulation
draw.rectangle((0, 0, 1920, 540), fill=BG_DARK)
draw.rectangle((0, 540, 1920, 1080), fill=BG_DARKER)

# Center circle
center_x, center_y = 960, 540
draw.ellipse((center_x-150, center_y-150, center_x+150, center_y+150), 
            fill=ACCENT_CYAN, outline=ACCENT_PURPLE, width=4)

try:
    font_splash = ImageFont.truetype("arial.ttf", 72)
    font_splash_sub = ImageFont.truetype("arial.ttf", 32)
except:
    font_splash = ImageFont.load_default()
    font_splash_sub = ImageFont.load_default()

# Title
draw.text((960, 700), "Air Canvas AI", fill=ACCENT_CYAN, font=font_splash, anchor="mm")

# Subtitle
draw.text((960, 800), "Draw with Your Hands", fill=LIGHT_GRAY, font=font_splash_sub, anchor="mm")

splash.save("assets/ui/splash.png")

# ------------------------
# Logo - Modern Design
# ------------------------

logo = Image.new("RGB", (1024, 1024), BG_DARK)
draw = ImageDraw.Draw(logo)

# Outer ring
draw.ellipse((100, 100, 924, 924), outline=ACCENT_CYAN, width=12)
draw.ellipse((100, 100, 924, 924), outline=ACCENT_PURPLE, width=4)

# Inner circle
draw.ellipse((250, 250, 774, 774), fill=ACCENT_CYAN, outline=0)
draw.ellipse((280, 280, 744, 744), fill=BG_DARK, outline=0)

# Text
try:
    font_logo = ImageFont.truetype("arial.ttf", 120)
except:
    font_logo = ImageFont.load_default()

draw.text((512, 512), "AC", fill=ACCENT_CYAN, font=font_logo, anchor="mm")

logo.save("assets/logo/logo.png")

print("✓ All assets generated successfully with modern design!")