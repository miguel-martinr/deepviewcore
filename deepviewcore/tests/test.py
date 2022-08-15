import cv2 as cv

from process.detect_objects import detect_objects_in_frame, draw_contours


cap = cv.VideoCapture("C:/Users/migue/Documents/U/4to/TFG/DeepView/static/videos/Pez1.mp4")

# Set frame index
cap.set(cv.CAP_PROP_POS_FRAMES, 55)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    [objects, frameHasEvent] = detect_objects_in_frame(frame, {"events": {"minArea": 200, "active": True}})

    draw_contours(frame, objects)
    if frameHasEvent:
        print("EVENT")
    else:
        print("NO EVENT")
    
    cv.imshow("frame", frame)
    if cv.waitKey(0) & 0xFF == ord('q'):
        break


print("Finished")
    # cv.imshow("Frame", frame)
    # if cv.waitKey(1) & 0xFF == ord('q'):
    #     break