import cv2 as cv
from process.preprocess_frame import preprocess_frame

def get_connected_components(frame):
  preprocessed_frame = preprocess_frame(frame)
  thresh = cv.threshold(preprocessed_frame, 20, 255, cv.THRESH_BINARY)[1]
  connected_components = cv.connectedComponentsWithStats(thresh, 4, cv.CV_32S)
  return connected_components


def detect_objects_in_frame(frame):
    preprocessed_frame = preprocess_frame(frame)

    thresh = cv.threshold(preprocessed_frame, 20, 255, cv.THRESH_BINARY)[1]

    cnts, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    return cnts


def draw_connected_components(frame, cc):
    (numLabels, labels, stats, centroids) = cc
    for i in range(1, numLabels):
      x = stats[i, cv.CC_STAT_LEFT]
      y = stats[i, cv.CC_STAT_TOP]
      w = stats[i, cv.CC_STAT_WIDTH]
      h = stats[i, cv.CC_STAT_HEIGHT]
      cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # for (x, y) in centroids:
    #     center = (int(x), int(y))
    #     cv.circle(frame, center, 5, (0, 255, 0), -1)
        
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
      
