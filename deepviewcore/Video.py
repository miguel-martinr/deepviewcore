from enum import Enum
import cv2 as cv
import time

from .process.detect_objects import detect_objects_in_frame, draw_contours


class DataFields:
  objects = "objects"    
class Video:

    def __init__(self, path: str):
        self.path = path
        self.cap = cv.VideoCapture(self.path, apiPreference=cv.CAP_FFMPEG)
        self.data = {
            DataFields.objects: [],
        }

        if not self.cap.isOpened():
            print(f"No se pudo abrir el vídeo \"{self.path}\"")
            exit(1)

    def __str__(self) -> str:
        return self.path

    def reset(self):
        self.cap.set(cv.CAP_PROP_POS_FRAMES, 0)

    def process(self, showContours: bool = False):
        print("Procesando vídeo...")

        cap = self.cap
        self.data[DataFields.objects] = []  # Reset contours_per_frame
        frameRate = int(self.getFrameRate())

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Detect objects
            # st = time.time()


            contours = detect_objects_in_frame(frame)
            objects = map(lambda cnt: {"circle": cv.minEnclosingCircle(cnt), "area": cv.contourArea(cnt)}, contours)

            # et = time.time()
            # print(f"Tiempo de ejecución: {et - st}")
            self.data[DataFields.objects].append(objects)

            # Draw contours
            if showContours:
                drawed = frame.copy()
                draw_contours(drawed, contours)
                cv.imshow("CC", drawed)
                if cv.waitKey(frameRate) & 0xFF == ord('q'):
                    break

        
        if (showContours):
            cv.destroyAllWindows()
        print("Vídeo procesado")

    def getConnectedComponents(self):
        return self.data["connected_components"]



    # Stats 

    def getStats(self):
        return {
            "path": self.path,
            "num_of_frames": self.numOfFrames(),
            "frame_rate": self.getFrameRate(),
            "duration_in_seconds": self.getDurationInSeconds(),
        }

    def numOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def getFrameRate(self):
        if self.cap:
          return self.cap.get(cv.CAP_PROP_FPS)
        return None

    def getDurationInSeconds(self):
        return self.numOfFrames() / self.getFrameRate()

