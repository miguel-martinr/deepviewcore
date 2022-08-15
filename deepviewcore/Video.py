from enum import Enum
import os
import cv2 as cv
import time

from .process.detect_objects import detect_objects_in_frame, draw_contours


class DataFields:
  frames = "frames"


defaultOptions = {
  "preprocess": {
    "top_hat": {
      "filterSize": (9, 9)
    },
    "denoise": None,
  },  

  "process": {},

  "events": {
    "minArea": 100,
    "active": True,
  }
}

class Video:

    def __init__(self, path: str):
        self.keep_processing = False
        self.path = path
        self.cap = cv.VideoCapture(self.path, apiPreference=cv.CAP_FFMPEG)
        self.data = {
            DataFields.frames: [],
        }

        self.frame_interval = 1 # Frame intevral for executing action passed to process method 
        if not self.cap.isOpened():
            print(f"No se pudo abrir el vídeo \"{self.path}\"")
            

    def __str__(self) -> str:
        return self.path

    def reset(self):
        self.cap.set(cv.CAP_PROP_POS_FRAMES, 0)

    def process(self, options = defaultOptions, action = lambda objects: None, showContours: bool = False):
        
        self.keep_processing = True
        cap = self.cap
        self.data[DataFields.frames] = []  # Reset contours_per_frame
        frameRate = int(self.getFrameRate())

        detectedEvents = []
        while cap.isOpened() and self.keep_processing:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Process frame
            [contours, objects, events] = self.processFrame(options=options, frame=frame)

            self.data[DataFields.frames].append(objects)
            detectedEvents.extend(events)

            if ((self.getCurrentFrameIndex() % self.frame_interval) == 0) or self.getCurrentFrameIndex() == self.numOfFrames() - 1:
              detectedObjects = self.data[DataFields.frames]              
              
              action([detectedObjects, detectedEvents])
              
              self.data[DataFields.frames] = []
              detectedEvents = []


            # Draw contours
            if showContours:
                drawed = frame.copy()
                draw_contours(drawed, contours)
                cv.imshow("CC", drawed)
                if cv.waitKey(frameRate) & 0xFF == ord('q'):
                    break

        if (showContours):
            cv.destroyAllWindows()
        

    def getConnectedComponents(self):
        return self.data["connected_components"]

    # Stats

    def getStats(self):
        """Gets video stats.
        A video stats is a dictionary with the following keys:
         - path: video path
         - size_in_MB: video size in MB
         - duration_in_seconds: video duration in seconds
         - fps: video frames per second
        """
        return {
            "path": self.path,
            "size_in_MB": self.getSizeInMB(),
            "duration_in_seconds": self.getDurationInSeconds(),
            "fps": self.getFrameRate(),
        }

    def getSizeInMB(self):
        return os.path.getsize(self.path) / (1024 * 1024)
        
    def numOfFrames(self):
        return int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

    def getFrameRate(self):
        if self.cap:
          return self.cap.get(cv.CAP_PROP_FPS)
        return None

    def getDurationInSeconds(self):
        return self.numOfFrames() / self.getFrameRate()

    def getCurrentFrameIndex(self):
        return int(self.cap.get(cv.CAP_PROP_POS_FRAMES)) - 1

    def stop_processing(self):
        self.keep_processing = False

    def setFrameIndex(self, newFrameIndex):
        self.cap.set(cv.CAP_PROP_POS_FRAMES, newFrameIndex + 1)

    def processFrame(self, options, frame = None):
        
        # Detect objects

        if frame is None:
          ret, frame = self.cap.read()
          if not ret:
            return [None, None]
            
        # st = time.time()
        
        contours = detect_objects_in_frame(frame, options=options)
        objects = map(lambda cnt: {"circle": cv.minEnclosingCircle(
            cnt), "area": cv.contourArea(cnt)}, contours)

        events = filter(lambda obj: obj["area"] > options["events"]["minArea"], objects)

        # et = time.time()
        # print(f"Tiempo de ejecución: {et - st}")
        return [contours, objects, events]



