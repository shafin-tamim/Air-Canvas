import cv2
import numpy as np
import os


class Toolbar:

    def __init__(self):
        self.toolbar_height = 150  # Increased for labels
        self.bg_color = (18, 18, 28)        # Dark background
        self.accent_color = (0, 188, 212)   # Cyan accent
        
        # Load asset images
        self.assets_path = "assets"
        self.icons = {}
        self.colors_img = {}
        
        # Load color swatches
        color_names = ["red", "green", "blue", "yellow", "purple"]
        for color in color_names:
            path = os.path.join(self.assets_path, "colors", f"{color}.png")
            if os.path.exists(path):
                self.colors_img[color] = cv2.imread(path)
        
        # Load toolbar icons
        icon_names = ["brush", "clear", "undo", "redo"]
        for icon in icon_names:
            path = os.path.join(self.assets_path, "icons", f"{icon}.png")
            if os.path.exists(path):
                self.icons[icon] = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        
        # Color to BGR mapping
        self.color_map = {
            "red": (59, 34, 255),
            "green": (89, 199, 52),
            "blue": (255, 122, 0),
            "yellow": (0, 204, 255),
            "purple": (222, 82, 175)
        }
        
        # Button positions - spaced out for better UX
        self.buttons = {
            "red": (15, 25, 85, 95),
            "green": (100, 25, 170, 95),
            "blue": (185, 25, 255, 95),
            "yellow": (270, 25, 340, 95),
            "purple": (355, 25, 425, 95),
            "brush": (450, 25, 520, 95),
            "clear": (535, 25, 605, 95),
            "undo": (620, 25, 690, 95),
            "redo": (705, 25, 775, 95),
        }

    def overlay_image(self, bg, overlay, x, y, width=80, height=80):
        """Overlay an image onto background"""
        if overlay is None:
            return bg
        
        # Resize overlay
        overlay_resized = cv2.resize(overlay, (width, height), interpolation=cv2.INTER_AREA)
        
        # Handle alpha channel if exists
        if overlay_resized.shape[2] == 4:  # RGBA
            alpha = overlay_resized[:, :, 3] / 255.0
            overlay_rgb = overlay_resized[:, :, :3]
            
            for c in range(3):
                bg[y:y+height, x:x+width, c] = (
                    overlay_rgb[:, :, c] * alpha +
                    bg[y:y+height, x:x+width, c] * (1 - alpha)
                )
        else:  # RGB
            bg[y:y+height, x:x+width] = overlay_resized
        
        return bg

    def draw_toolbar(self, img):
        """Draw modern toolbar with asset images and labels"""
        h, w, _ = img.shape

        # Create toolbar area
        toolbar = np.zeros((self.toolbar_height, w, 3), dtype=np.uint8)
        toolbar[:] = self.bg_color

        # Top accent line - thicker and more visible
        cv2.line(toolbar, (0, 0), (w, 0), self.accent_color, 6)
        
        # Bottom border line
        cv2.line(toolbar, (0, self.toolbar_height-3), (w, self.toolbar_height-3), self.accent_color, 3)

        # Draw color buttons with labels
        color_order = [
            ("red", "RED", (59, 34, 255)),
            ("green", "GREEN", (89, 199, 52)),
            ("blue", "BLUE", (255, 122, 0)),
            ("yellow", "YELLOW", (0, 204, 255)),
            ("purple", "PURPLE", (222, 82, 175)),
        ]
        
        for color_name, color_label, color_rgb in color_order:
            x, y, x2, y2 = self.buttons[color_name]
            
            # Draw button shadow for depth
            cv2.rectangle(toolbar, (x-4, y+3), (x2+4, y2+3), (10, 10, 15), -1)
            
            # Draw button background
            cv2.rectangle(toolbar, (x-4, y-4), (x2+4, y2+4), (30, 30, 40), -1)
            
            # Draw button border with accent color
            cv2.rectangle(toolbar, (x-4, y-4), (x2+4, y2+4), self.accent_color, 3)
            
            # Draw color swatch
            if color_name in self.colors_img:
                self.overlay_image(toolbar, self.colors_img[color_name], x, y, 
                                 width=(x2-x), height=(y2-y))
            else:
                # Fallback: draw colored circle
                cv2.circle(toolbar, ((x+x2)//2, (y+y2)//2), 30, 
                          color_rgb, -1)
            
            # Add color label below button
            text_x = x + (x2-x)//2 - 20
            text_y = y2 + 20
            cv2.putText(toolbar, color_label, (text_x, text_y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.35, 
                       (150, 150, 150), 1)

        # Draw tool buttons with better styling
        tool_buttons = [
            ("brush", "BRUSH", "🖌️"),
            ("clear", "CLEAR", "🗑️"),
            ("undo", "UNDO", "↶"),
            ("redo", "REDO", "↷"),
        ]
        
        for icon_name, tool_label, emoji in tool_buttons:
            x, y, x2, y2 = self.buttons[icon_name]
            
            # Draw button shadow for depth
            cv2.rectangle(toolbar, (x-4, y+3), (x2+4, y2+3), (10, 10, 15), -1)
            
            # Draw button background
            cv2.rectangle(toolbar, (x-4, y-4), (x2+4, y2+4), (40, 40, 50), -1)
            
            # Draw button border with accent color
            cv2.rectangle(toolbar, (x-4, y-4), (x2+4, y2+4), self.accent_color, 3)
            
            # Draw icon
            if icon_name in self.icons:
                self.overlay_image(toolbar, self.icons[icon_name], x, y, 
                                 width=80, height=80)
            else:
                # Fallback: draw symbol
                cv2.putText(toolbar, emoji, (x+15, y+45),
                           cv2.FONT_HERSHEY_SIMPLEX, 1.2, 
                           self.accent_color, 2)
            
            # Add tool label below button
            text_x = x + (x2-x)//2 - 18
            text_y = y2 + 20
            cv2.putText(toolbar, tool_label, (text_x, text_y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.35,
                       (150, 150, 150), 1)

        # Merge toolbar with original image
        img[0:self.toolbar_height] = toolbar
        
        return img

    def check_click(self, x, y):
        """Check which button was clicked"""
        
        if y > self.toolbar_height or y < 10:
            return None

        # Check color buttons
        for color in ["red", "green", "blue", "yellow", "purple"]:
            x1, y1, x2, y2 = self.buttons[color]
            if x1 <= x <= x2 and y1 <= y <= y2:
                return color.upper()

        # Check tool buttons
        tool_map = {
            "brush": "BRUSH",
            "clear": "CLEAR",
            "undo": "UNDO",
            "redo": "REDO",
        }
        
        for tool in ["brush", "clear", "undo", "redo"]:
            x1, y1, x2, y2 = self.buttons[tool]
            if x1 <= x <= x2 and y1 <= y <= y2:
                return tool_map[tool]

        return None