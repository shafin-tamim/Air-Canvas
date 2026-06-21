import cv2
import numpy as np


class DrawingEngine:

    def __init__(self):
        self.canvas = None

        self.current_color = (0, 204, 255)  # Modern cyan
        self.brush_size = 6

        self.undo_stack = []
        self.redo_stack = []

    def create_canvas(self, frame):

        if self.canvas is None:
            h, w, _ = frame.shape
            self.canvas = np.zeros(
                (h, w, 3),
                dtype=np.uint8
            )

    def save_state(self):

        if self.canvas is not None:
            self.undo_stack.append(
                self.canvas.copy()
            )

            if len(self.undo_stack) > 20:
                self.undo_stack.pop(0)

    def draw(self, x1, y1, x2, y2):

        cv2.line(
            self.canvas,
            (x1, y1),
            (x2, y2),
            self.current_color,
            self.brush_size,
            cv2.LINE_AA  # Anti-aliased line
        )

    def erase(self, x1, y1, x2, y2):

        cv2.line(
            self.canvas,
            (x1, y1),
            (x2, y2),
            (0, 0, 0),
            40,
            cv2.LINE_AA  # Anti-aliased line
        )

    def clear(self):

        if self.canvas is not None:
            self.save_state()
            self.canvas[:] = 0

    def undo(self):

        if len(self.undo_stack):

            self.redo_stack.append(
                self.canvas.copy()
            )

            self.canvas = self.undo_stack.pop()

    def redo(self):

        if len(self.redo_stack):

            self.undo_stack.append(
                self.canvas.copy()
            )

            self.canvas = self.redo_stack.pop()

    def merge(self, frame):

        self.create_canvas(frame)

        return cv2.addWeighted(
            frame,
            0.7,
            self.canvas,
            1,
            0
        )