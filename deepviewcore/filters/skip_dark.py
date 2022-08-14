import cv2 as cv
import numpy as np

def skip_dark(frame, options=None):
  if frame is None:
      return None

  # Occupy 24,88% if the image
  rectangles = [
  ((157, 200), (587, 440)),
  ((744, 420), (1174, 660)),
  ((1331, 200), (1761, 440)),
  ((157, 640), (587, 880)),
  ((1331, 640), (1761, 880))
  ]

  mean_areas = []
  for left_top, right_bottom in rectangles:
    mean_areas.extend(frame[left_top[0]:right_bottom[0]][left_top[1]:right_bottom[1]])

  min_brightness = options.get("min_brightness")
  if min_brightness is None:
    min_brightness = 1


  # Calculate brightness
  brightness = np.mean(mean_areas)
  return frame


filter = {
  "name": "skip_dark",
  "filter": skip_dark,
  "options": {"min_brightness": 1}
}
