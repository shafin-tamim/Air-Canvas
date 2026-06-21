import os

project_name = "AirCanvasAI"

folders = [
    f"{project_name}/core",

    f"{project_name}/assets/colors",
    f"{project_name}/assets/icons",
    f"{project_name}/assets/gestures",
    f"{project_name}/assets/ui",
    f"{project_name}/assets/logo",

    f"{project_name}/saved/images",
    f"{project_name}/saved/videos"
]

files = [
    f"{project_name}/main.py",

    f"{project_name}/core/hand_tracker.py",
    f"{project_name}/core/gesture_detector.py",
    f"{project_name}/core/drawing_engine.py",
    f"{project_name}/core/toolbar.py",
    f"{project_name}/core/recorder.py",
    f"{project_name}/core/export_manager.py",

    f"{project_name}/requirements.txt"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    with open(file, "w", encoding="utf-8") as f:
        pass

print("✅ AirCanvasAI project structure created successfully!")