import cv2
import os
from datetime import datetime


class ExportManager:

    def __init__(self):

        self.save_dir = "saved/images"

        os.makedirs(
            self.save_dir,
            exist_ok=True
        )

    def save_png(self, canvas):

        if canvas is None:
            print("❌ Canvas is empty!")
            return None

        filename = os.path.join(
            self.save_dir,
            datetime.now().strftime(
                "%Y%m%d_%H%M%S.png"
            )
        )

        success = cv2.imwrite(
            filename,
            canvas
        )

        if success:
            print(f"✅ Saved: {filename}")
            return filename

        print("❌ Failed to save image")
        return None