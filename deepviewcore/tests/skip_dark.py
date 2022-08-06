import cv2 as cv


def drawRectangle(frame, p1, p2, color = (0, 255, 0), thickness = 2):
  cv.rectangle(frame, p1, p2, color, thickness)

cap = cv.VideoCapture(
    "C:/Users/migue/Documents/U/4to/TFG/DeepView/static/videos/plancton_1.mp4")


ret, frame = cap.read()
# Ocuppy 27,78 % of the area
# rectangles = [
#   ((120, 90), (600, 330)),
#   ((720, 420), (1200, 660)),
#   ((1320, 90), (1800, 330)),
#   ((120, 750), (600, 990)),
#   ((1320, 750), (1800, 990)),
# ]


# Occupy 24,88% of the area
rectangles = [
  ((157, 200), (587, 440)),
  ((744, 420), (1174, 660)),
  ((1331, 200), (1761, 440)),
  ((157, 640), (587, 880)),
  ((1331, 640), (1761, 880))
]

for p1, p2 in rectangles:
  drawRectangle(frame, p1, p2)

window = cv.namedWindow("Frame", cv.WINDOW_NORMAL)
cv.imshow("Frame", frame)
cv.waitKey(0)
# cv.imshow("Frame", frame)
# if cv.waitKey(1) & 0xFF == ord('q'):
#     break
