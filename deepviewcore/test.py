import cv2 as cv

from process.detect_objects import detect_objects_in_frame


cap = cv.VideoCapture("C:/Users/migue/Documents/U/4to/TFG/DeepView/static/videos/plancton_1.mp4")


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    objects = detect_objects_in_frame(frame)

print("Finished")
    # cv.imshow("Frame", frame)
    # if cv.waitKey(1) & 0xFF == ord('q'):
    #     break