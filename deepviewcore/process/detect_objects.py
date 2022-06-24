import cv2 as cv
from .preprocess_frame import preprocess_frame


defaultOptions = {
  "preprocess": {
    "top_hat": {
      "filterSize": (2, 2)
    },

    "to_gray": None,
    "denoise": None,
  },  
}

def detect_objects_in_frame(frame, options = defaultOptions):
    preprocessed_frame = preprocess_frame(frame, options["preprocess"])

    thresh = cv.threshold(preprocessed_frame, 20, 255, cv.THRESH_BINARY)[1]

    cnts, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return cnts
    
        
def draw_contours(frame, contours):
    for cnt in contours:
      (x, y), radius = cv.minEnclosingCircle(cnt)
      center = (int(x), int(y))
      radius = int(radius)
      radius = int(radius + (radius * 2))
      
      area = "{:6.2f}".format(cv.contourArea(cnt))
      font = cv.FONT_HERSHEY_SIMPLEX
      cv.putText(frame, area, (int(x + radius), int(y + radius)), font, 0.5, (0, 255, 0), 2, cv.LINE_AA)
      cv.circle(frame, center, radius, (0, 255, 0), 2)
      
