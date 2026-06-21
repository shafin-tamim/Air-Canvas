import cv2
import os
from datetime import datetime


class ScreenRecorder:

    def __init__(self):

        self.recording = False
        self.writer = None

        os.makedirs(
            "saved/videos",
            exist_ok=True
        )

    def start(self, width, height):

        filename = datetime.now().strftime(
            "saved/videos/%Y%m%d_%H%M%S.mp4"
        )

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        self.writer = cv2.VideoWriter(
            filename,
            fourcc,
            20,
            (width, height)
        )

        self.recording = True

        print("Recording Started")

    def write(self, frame):

        if self.recording:
            self.writer.write(frame)

    def stop(self):

        if self.writer:
            self.writer.release()

        self.recording = False

        print("Recording Stopped")