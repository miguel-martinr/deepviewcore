import cv2 as cv

def threshold(frame, options):
  thresh = options['thresh']
  maxValue = options['maxValue']

  thresh_frame = cv.threshold(frame, thresh, maxValue, cv.THRESH_BINARY)[1]
  return thresh_frame


filter = {
  "name": "threshold",
  "filter": threshold,
  "options": {
    "thresh": 20,
    "maxValue": 255,
  }
}