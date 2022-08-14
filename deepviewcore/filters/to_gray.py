import cv2 as cv


def to_gray(frame, options=None):
    if frame is None:
      return None
      
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)    
    return gray

filter = {
  "name": "to_gray",
  "filter": to_gray,
  "options": None,
}
