import cv2
import numpy as np


class Toolbar:

    def __init__(self):

        self.height = 80

        self.bg_color = (30, 30, 35)
        self.border = (0, 200, 255)
        self.text = (255, 255, 255)

        self.buttons = [
            ("RED", (0, 0, 255)),
            ("GREEN", (0, 255, 0)),
            ("BLUE", (255, 0, 0)),
            ("YELLOW", (0, 255, 255)),
            ("PURPLE", (255, 0, 255)),
            ("CLEAR", None),
            ("UNDO", None),
            ("REDO", None)
        ]

    def draw_toolbar(self, img):

        h, w = img.shape[:2]

        cv2.rectangle(
            img,
            (0, 0),
            (w, self.height),
            self.bg_color,
            -1
        )

        cv2.line(
            img,
            (0, self.height),
            (w, self.height),
            self.border,
            2
        )

        margin = 10
        btn_w = 70
        btn_h = 50
        gap = 10

        self.button_rects = {}

        x = margin

        for name, color in self.buttons:

            y = 15

            cv2.rectangle(
                img,
                (x, y),
                (x + btn_w, y + btn_h),
                (60, 60, 60),
                -1
            )

            cv2.rectangle(
                img,
                (x, y),
                (x + btn_w, y + btn_h),
                self.border,
                2
            )

            if color is not None:

                cv2.circle(
                    img,
                    (x + btn_w // 2, y + btn_h // 2),
                    18,
                    color,
                    -1
                )

            else:

                cv2.putText(
                    img,
                    name,
                    (x + 6, y + 32),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.45,
                    self.text,
                    1,
                    cv2.LINE_AA
                )

            self.button_rects[name] = (
                x,
                y,
                x + btn_w,
                y + btn_h
            )

            x += btn_w + gap

    def check_click(self, x, y):

        if y > self.height:
            return None

        for name, rect in self.button_rects.items():

            x1, y1, x2, y2 = rect

            if x1 <= x <= x2 and y1 <= y <= y2:

                return name

        return None