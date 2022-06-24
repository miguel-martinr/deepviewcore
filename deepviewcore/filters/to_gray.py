import cv2 as cv


def to_gray(frame, options=None):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    return gray
