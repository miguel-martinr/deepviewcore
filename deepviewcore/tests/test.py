import cv2 as cv

from deepviewcore.process.detect_objects import detect_objects_in_frame, draw_contours


cap = cv.VideoCapture("C:/Users/migue/Documents/U/4to/TFG/DeepView/static/videos/plancton_1.mp4")

# Set frame index
cap.set(cv.CAP_PROP_POS_FRAMES, 33)
window = cv.namedWindow("Frame", cv.WINDOW_NORMAL)

while cap.isOpened():
    ret, frame = cap.read()
    
    contours = detect_objects_in_frame(frame, {})
    draw_contours(frame, contours)

    cv.imshow("Frame", frame)

    
    if cv.waitKey(0) & 0xFF == ord('q'):
        break


print("Finished")
    # cv.imshow("Frame", frame)
    # if cv.waitKey(1) & 0xFF == ord('q'):
    #     break