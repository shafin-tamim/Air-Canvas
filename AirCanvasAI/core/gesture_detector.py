class GestureDetector:

    @staticmethod
    def detect(fingers):

        if not fingers or len(fingers) != 5:
            return "NONE"

        # 👍 Save
        if fingers == [1, 0, 0, 0, 0]:
            return "SAVE"

        # ☝️ Draw
        elif fingers == [0, 1, 0, 0, 0]:
            return "DRAW"

        # ✌️ Selection / Move
        elif fingers == [0, 1, 1, 0, 0]:
            return "MOVE"

        # 🖐️ Erase
        elif fingers == [1, 1, 1, 1, 1]:
            return "ERASE"

        # ✊ Pause
        elif fingers == [0, 0, 0, 0, 0]:
            return "PAUSE"

        # 🤟 Record
        elif fingers == [1, 1, 0, 0, 1]:
            return "RECORD"

        # Three fingers
        elif fingers == [0, 1, 1, 1, 0]:
            return "MENU"

        return "UNKNOWN"