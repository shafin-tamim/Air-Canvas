import cv2
import mediapipe as mp


class HandTracker:

    def __init__(
        self,
        mode=False,
        maxHands=1,
        detectionCon=0.7,
        trackCon=0.7
    ):

        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )

        self.mpDraw = mp.solutions.drawing_utils

        self.tipIds = [4, 8, 12, 16, 20]

        self.landmark_list = []
        self.results = None

    def find_hands(self, img, draw=True):

        imgRGB = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2RGB
        )

        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:

            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(
                        img,
                        handLms,
                        self.mpHands.HAND_CONNECTIONS
                    )

        return img

    def find_position(self, img):

        self.landmark_list = []

        if (
            self.results is not None
            and self.results.multi_hand_landmarks
        ):

            myHand = self.results.multi_hand_landmarks[0]

            h, w, _ = img.shape

            for idx, lm in enumerate(myHand.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                self.landmark_list.append(
                    [idx, cx, cy]
                )

        return self.landmark_list

    def fingers_up(self):

        if len(self.landmark_list) < 21:
            return []

        fingers = []

        # Thumb
        if (
            self.landmark_list[4][1]
            > self.landmark_list[3][1]
        ):
            fingers.append(1)
        else:
            fingers.append(0)

        # Index, Middle, Ring, Pinky
        for tip in [8, 12, 16, 20]:

            if (
                self.landmark_list[tip][2]
                < self.landmark_list[tip - 2][2]
            ):
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def get_index_tip(self):

        if len(self.landmark_list) >= 9:

            return (
                self.landmark_list[8][1],
                self.landmark_list[8][2]
            )

        return None

    def get_middle_tip(self):

        if len(self.landmark_list) >= 13:

            return (
                self.landmark_list[12][1],
                self.landmark_list[12][2]
            )

        return None