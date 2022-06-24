import cv2 as cv

from deepviewcore.process.process_frame import process_frame
from .preprocess_frame import preprocess_frame


def detect_objects_in_frame(frame, options):

    preprocess_options = options.get("preprocess")
    process_options = options.get("process")

    if preprocess_options is None:
      preprocess_options = {}
    if process_options is None:
      process_options = {}

    preprocessed_frame = preprocess_frame(frame, preprocess_options)

    processed_frame = process_frame(preprocessed_frame, process_options)

    cnts, _ = cv.findContours(processed_frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
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
      
