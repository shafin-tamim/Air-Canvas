import cv2
import numpy as np

from core.hand_tracker import HandTracker
from core.gesture_detector import GestureDetector
from core.drawing_engine import DrawingEngine
from core.toolbar import Toolbar

# Initialize camera
cap = cv2.VideoCapture(0)

# Set camera resolution for larger window
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("❌ Camera not found!")
    print("Please connect your webcam and try again.")
    exit()

print("✅ Camera initialized")
print("📸 Starting Air Canvas AI...")

tracker = HandTracker()
engine = DrawingEngine()
toolbar = Toolbar()

# Window setup
window_name = "Air Canvas AI"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(window_name, 1280, 820)

xp, yp = 0, 0
fps_counter = 0
fps = 0

while True:

    success, frame = cap.read()

    if not success:
        print("❌ Failed to read from camera")
        break

    frame = cv2.flip(frame, 1)
    
    # Get frame dimensions for resizing if needed
    h, w, _ = frame.shape

    # Create canvas first time
    engine.create_canvas(frame)

    tracker.find_hands(frame)

    lmList = tracker.find_position(frame)

    fingers = tracker.fingers_up()

    gesture = GestureDetector.detect(fingers)

    toolbar.draw_toolbar(frame)

    if lmList:

        tip = tracker.get_index_tip()

        if tip is not None:

            x, y = tip

            # Toolbar Click
            if y < 150:

                action = toolbar.check_click(x, y)

                if action == "RED":
                    engine.current_color = (59, 34, 255)

                elif action == "GREEN":
                    engine.current_color = (89, 199, 52)

                elif action == "BLUE":
                    engine.current_color = (255, 122, 0)

                elif action == "YELLOW":
                    engine.current_color = (0, 204, 255)

                elif action == "PURPLE":
                    engine.current_color = (222, 82, 175)

                elif action == "CLEAR":
                    engine.clear()

                elif action == "UNDO":
                    engine.undo()

                elif action == "REDO":
                    engine.redo()

                elif action == "BRUSH":
                    pass  # Just a toggle button

            # Draw
            elif gesture == "DRAW":

                if xp == 0 and yp == 0:
                    xp, yp = x, y

                engine.draw(
                    xp,
                    yp,
                    x,
                    y
                )

                xp, yp = x, y

            # Erase
            elif gesture == "ERASE":

                if xp == 0 and yp == 0:
                    xp, yp = x, y

                engine.erase(
                    xp,
                    yp,
                    x,
                    y
                )

                xp, yp = x, y

            else:
                xp, yp = 0, 0

    output = engine.merge(frame)

    # Modern status display
    gesture_icons = {
        "DRAW": "✏️",
        "ERASE": "🗑️",
        "MOVE": "➡️",
        "IDLE": "⏸️"
    }
    
    gesture_display = gesture if gesture else "IDLE"
    icon = gesture_icons.get(gesture_display, "⏸️")
    
    # Status display area (moved down due to taller toolbar)
    cv2.putText(
        output,
        f"{icon} {gesture_display}",
        (20, 185),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 188, 212),
        2
    )
    
    # Show current color
    cv2.putText(
        output,
        "Color:",
        (20, 215),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (150, 150, 150),
        1
    )
    cv2.circle(output, (100, 210), 8, engine.current_color, -1)
    cv2.circle(output, (100, 210), 8, (0, 188, 212), 2)

    # Add help text at bottom
    help_text = "Click colors to change | Press Q or close window to exit"
    cv2.putText(
        output,
        help_text,
        (10, h - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (150, 150, 150),
        1
    )

    # Display the output
    cv2.imshow(window_name, output)

    # Handle keyboard input
    key = cv2.waitKey(1) & 0xFF
    
    # Exit on 'q', ESC, or window close
    if key == ord('q') or key == 27:  # 'q' or ESC
        print("\n✅ Closing application...")
        break
    
    # Check if window is closed (window close button)
    try:
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            print("\n✅ Window closed, exiting...")
            break
    except:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("✅ Air Canvas AI closed successfully!")
