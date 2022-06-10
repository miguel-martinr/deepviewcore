from msilib.schema import Error
from sys import api_version
import cv2 as cv

from process.detect_objects import detect_objects_in_frame, draw_contours


class Video:

    def __init__(self, path: str):
        self.path = path
        self.cap = cv.VideoCapture(self.path, apiPreference=cv.CAP_FFMPEG)
        self.data = {
            "contours_per_frame": [],
        }

        if not self.cap.isOpened():
            print(f"No se pudo abrir el vídeo \"{self.path}\"")
            exit(1)

    def numOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def __str__(self) -> str:
        return self.path

    def reset(self):
        self.cap.set(cv.CAP_PROP_POS_FRAMES, 0)


    def process(self, showContours: bool = False):
        print("Procesando vídeo...")

        cap = self.cap
        self.data["contours_per_frame"] = []  # Reset contours_per_frame

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Detect objects
            contours = detect_objects_in_frame(frame)
            self.data["contours_per_frame"].append(contours)

            # Draw contours
            if showContours:
                drawed = frame.copy()
                draw_contours(drawed, contours)
                cv.imshow("Contours", drawed)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break

        
        if (showContours):
            cv.destroyAllWindows()
        print("Vídeo procesado")

