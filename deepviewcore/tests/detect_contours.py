import cv2 as cv
from deepviewcore.process.detect_objects import detect_objects_in_frame

video_path = "C:/Users/migue/Documents/U/4to/TFG/DeepView/static/videos/Luz On-Off.mp4"

cap = cv.VideoCapture(video_path)

ret, frame = cap.read()

cnts = detect_objects_in_frame(frame, {})


