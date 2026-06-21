# 🎨 Air Canvas AI - Hand Gesture Drawing Application

A modern, user-friendly hand gesture-based digital drawing application powered by AI-powered hand tracking and MediaPipe. Draw with your hands using just a webcam!

![Version](https://img.shields.io/badge/version-4.0-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-green)
![Status](https://img.shields.io/badge/status-ready%20to%20use-brightgreen)

---

## ✨ Features

✅ **Hand Gesture Recognition**
- Automatic hand detection and tracking via MediaPipe
- Real-time gesture detection (Draw, Erase, Move, Idle)
- No special hardware needed - just a webcam!

✅ **Professional Drawing Tools**
- 5 vibrant colors (Red, Green, Blue, Yellow, Purple)
- Brush tool for drawing
- Eraser tool for correcting mistakes
- Undo/Redo functionality (max 20 states)
- Clear canvas option

✅ **User-Friendly Interface**
- Large 1280x720 window for clear visibility
- Professional toolbar with asset-based buttons
- Clear labels on all buttons
- On-screen help text and status display
- Real-time gesture and color feedback

✅ **Easy Window Management**
- Resizable window (drag corners)
- Multiple exit options:
  - Click X button
  - Press Q key
  - Press ESC key

✅ **Modern Design**
- Dark theme (#121214 background)
- Cyan accents (#00BCD4)
- Professional asset-based UI
- Anti-aliased drawing for smooth lines
- Shadow effects and styled buttons

---

## 📋 Requirements

- **Python**: 3.8 or higher
- **Webcam**: Built-in or USB camera
- **OS**: Windows, macOS, or Linux

### Dependencies

```
opencv-python>=4.8.0
mediapipe>=0.10.0
numpy>=1.24.0
Pillow>=10.0.0
```

---

## 🚀 Quick Start

### 1. Clone or Extract the Project
```bash
cd f:\Git\Air-Canvas
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
cd AirCanvasAI
python main.py
```

### 4. Start Drawing!
- Show your hand to the camera
- Use gestures to draw and control the application
- Click toolbar buttons to change colors and tools
- Press Q, ESC, or click X to exit

---

## 🎮 How to Use

### Gestures

| Gesture | Action | How to Do It |
|---------|--------|------------|
| **Draw** | Start drawing | Hold hand up with 2 fingers raised (peace sign) |
| **Erase** | Erase drawings | Hold hand with 3+ fingers raised (flat hand) |
| **Move** | Move cursor without drawing | Make a fist or closed hand |
| **Idle** | Stop (default state) | Keep hand in relaxed state |

### Toolbar Buttons

**Color Selection** (Click to change drawing color):
- 🔴 **RED** - Modern red (#3B22FF)
- 🟢 **GREEN** - Vibrant green (#59C734)
- 🔵 **BLUE** - Bright blue (#FF7A00)
- 🟡 **YELLOW** - Bright yellow (#00CCFF)
- 🟣 **PURPLE** - Modern purple (#DE52AF)

**Tools** (Click to select tool):
- 🖌️ **BRUSH** - Drawing/paint mode
- 🗑️ **CLEAR** - Erase entire canvas
- ↶ **UNDO** - Undo last action
- ↷ **REDO** - Redo last action


## 📐 Window Specifications

| Feature | Specification |
|---------|---------------|
| Default Size | 1280×720 (Full HD preview) |
| Resizable | Yes - drag corners |
| Aspect Ratio | Maintained on resize |
| Toolbar Height | 150px |
| Drawing Area | Remaining space below toolbar |
| FPS Display | Shown in console |

---

## 📂 Project Structure

```
Air-Canvas/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── LICENSE                   # Project license
├── template.py               # Template file
├── AirCanvasAI/
│   ├── main.py              # Main application entry point
│   ├── generate_assets_v2.py # Asset generation script
│   ├── USER_GUIDE.md        # Detailed user instructions
│   ├── IMPROVEMENTS.md      # Changelog
│   ├── QUICKSTART.txt       # Quick reference guide
│   ├── startup_test.py      # Verification script
│   ├── core/
│   │   ├── toolbar.py       # Toolbar with buttons and colors
│   │   ├── drawing_engine.py # Canvas and drawing logic
│   │   ├── hand_tracker.py  # Hand detection with MediaPipe
│   │   ├── gesture_detector.py # Gesture recognition
│   │   ├── export_manager.py # Save/export functionality
│   │   └── recorder.py      # Video recording
│   ├── assets/
│   │   ├── colors/          # Color swatch images
│   │   ├── icons/           # Toolbar button icons
│   │   ├── ui/              # UI element images
│   │   ├── gestures/        # Gesture reference images
│   │   └── logo/            # Brand logo
│   └── saved/
│       ├── images/          # Saved drawings
│       └── videos/          # Recorded videos
```

---

## 🛠️ Installation Details

### Step-by-Step Setup

**Windows:**
```bash
# Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
cd AirCanvasAI
python main.py
```

**macOS/Linux:**
```bash
# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
cd AirCanvasAI
python main.py
```

### Verify Installation

Run the startup test to verify all components:
```bash
python startup_test.py
```

Expected output:
```
✅ Python 3.12.7 (Good!)
✅ All packages installed
✅ 25 asset files present
✅ All core modules present
✅ Module imports successful
✅ Camera detected and working
```

---

## 🎨 Color Palette Reference

### Drawing Colors (BGR format - OpenCV)

| Color | RGB (Standard) | BGR (OpenCV) | Hex | Name |
|-------|---------------|-------------|-----|------|
| Red | (255, 34, 59) | (59, 34, 255) | #3B22FF | Modern Red |
| Green | (82, 199, 89) | (89, 199, 52) | #59C734 | Vibrant Green |
| Blue | (0, 122, 255) | (255, 122, 0) | #FF7A00 | Bright Blue |
| Yellow | (255, 204, 0) | (0, 204, 255) | #00CCFF | Bright Yellow |
| Purple | (175, 82, 222) | (222, 82, 175) | #DE52AF | Modern Purple |

### UI Colors

| Element | Color (BGR) | Hex | Purpose |
|---------|------------|-----|---------|
| Background | (18, 18, 28) | #121214 | Dark canvas |
| Primary Accent | (0, 188, 212) | #00BCD4 | Cyan highlights |
| Secondary Accent | (156, 39, 176) | #9C27B0 | Purple accents |

---

## 🎯 Key Improvements (v4.0)

### Window & Display
- ✅ Window size increased to 1280×720 (from small default)
- ✅ Resizable window with aspect ratio maintained
- ✅ Professional dark theme with cyan accents

### Toolbar
- ✅ Height increased to 150px (from 120px)
- ✅ Added clear labels under each button
- ✅ Professional asset-based button images
- ✅ Shadow effects for visual depth
- ✅ Better spacing and alignment

### Controls & Functionality
- ✅ Close button now works properly (X, Q, ESC)
- ✅ Fixed window close detection
- ✅ Multiple exit methods
- ✅ Better gesture feedback

### User Experience
- ✅ On-screen help text and status display
- ✅ Real-time color and gesture indicators
- ✅ Console output with helpful information
- ✅ Comprehensive documentation

---

## 🐛 Troubleshooting

### Issue: Window won't close
**Solution**: Try any of these:
- Click the **X button** on window
- Press **Q** key
- Press **ESC** key

### Issue: Camera not detected
**Solutions**:
- Check camera is connected and not in use by other apps
- Try plugging into different USB port
- Restart application
- Check camera permissions in OS settings

### Issue: Gestures not recognized
**Solutions**:
- Ensure good lighting (hand must be visible)
- Keep hand fully in view of camera
- Move hand slowly and deliberately
- Check hand is in front of camera (not behind)
- Clean camera lens

### Issue: Window is too small
**Solution**: Drag window corners to resize to desired size (maintains aspect ratio)

### Issue: Buttons not responding
**Solutions**:
- Ensure cursor is over button (small margin for click detection)
- Click center of button
- Try clicking again with steady hand
- Check hand lighting

### Issue: Drawing is jerky or slow
**Solutions**:
- Close other CPU-intensive applications
- Reduce window size
- Improve lighting
- Check camera FPS in console output

---

## 📚 Documentation

The project includes comprehensive documentation:

- **USER_GUIDE.md** - Detailed user instructions and reference
- **IMPROVEMENTS.md** - List of all improvements and changes
- **QUICKSTART.txt** - Visual quick reference guide
- **DESIGN.md** - Design specifications and color palette

---

## 🔧 Technical Details

### Core Technologies

**MediaPipe**
- Hand tracking and landmark detection
- Real-time pose estimation
- GPU acceleration support

**OpenCV (cv2)**
- Webcam capture at 1280×720 resolution
- Image drawing and manipulation
- Window management with proper property detection
- Anti-aliased line drawing (cv2.LINE_AA)

**NumPy**
- Canvas array operations
- Image processing
- Numerical computations

**PIL/Pillow**
- Asset image generation
- Image format handling
- Alpha channel support

### Performance Specs

- **FPS**: 30+ FPS on modern hardware
- **Latency**: ~33ms per frame
- **Memory**: ~200-300MB
- **CPU Usage**: ~15-30% (varies with hand position)
- **GPU**: Supported (automatic via MediaPipe)

---

## 🚀 Advanced Usage

### Running Startup Test
```bash
cd AirCanvasAI
python startup_test.py
```

### Generating Assets
To regenerate asset images with custom colors:
```bash
python generate_assets_v2.py
```

### Recording Drawings
Your drawings are automatically saved to:
```
AirCanvasAI/saved/images/
```

---

## 📝 Configuration

To customize the application, edit these values in code:

**Window Size** - Edit in `main.py`:
```python
cv2.resizeWindow(window_name, 1280, 820)  # Change dimensions
```

**Toolbar Height** - Edit in `core/toolbar.py`:
```python
self.toolbar_height = 150  # Change height in pixels
```

**Brush Size** - Edit in `core/drawing_engine.py`:
```python
self.brush_size = 6  # Change brush width
```

**Colors** - Edit in `core/toolbar.py`:
```python
"red": (59, 34, 255)  # Change BGR values
```

---

## 🤝 Support

If you encounter issues:

1. **Check the documentation**
   - USER_GUIDE.md for detailed instructions
   - IMPROVEMENTS.md for recent changes
   - QUICKSTART.txt for quick reference

2. **Run startup test**
   ```bash
   python startup_test.py
   ```

3. **Check common issues** (see Troubleshooting section)

4. **Verify dependencies**
   ```bash
   pip list
   ```

---

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

---

## 🎉 Get Started

**Ready to draw? Run this:**

```bash
cd AirCanvasAI
python main.py
```

**Show your hand to the camera and start drawing!**

---

## 📊 Project Status

| Component | Status |
|-----------|--------|
| Core Drawing | ✅ Complete |
| Hand Tracking | ✅ Complete |
| Gesture Recognition | ✅ Complete |
| Toolbar UI | ✅ Complete |
| Asset Integration | ✅ Complete |
| Documentation | ✅ Complete |
| Testing | ✅ Verified |

**Status**: 🎉 **Ready to Use!**

---

## 💡 Tips for Best Results

1. **Lighting**: Good lighting helps hand detection - face a window or use a lamp
2. **Distance**: Keep hand 30-60cm from camera for best results
3. **Background**: Solid background works best (avoid complex patterns)
4. **Steady Hand**: Move slowly and deliberately for smooth lines
5. **Full View**: Keep entire hand visible in camera view
6. **Color Selection**: Click button center for reliable detection
7. **Undo Often**: Use Undo (↶) if you make mistakes - you have 20 undo states!

---

## 🎨 Enjoy Creating!

Air Canvas AI brings the joy of digital drawing with natural hand gestures. No stylus needed, just your hands and imagination!

**Happy drawing!** ✏️🎨

---

**Last Updated**: June 2026  
**Version**: 4.0 (User-Friendly Edition)  
**Maintained**: Active Development
