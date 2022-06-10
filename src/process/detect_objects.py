import cv2 as cv

from process.filters.top_hat import top_hat
from process.preprocess_frame import preprocess_frame


def detect_objects_in_frame(frame):
    preprocessed_frame = preprocess_frame(frame)

    thresh = cv.threshold(preprocessed_frame, 20, 255, cv.THRESH_BINARY)[1]

    cnts, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # cnts = cnts[0] if len(cnts) == 2 else cnts[1]
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
      
