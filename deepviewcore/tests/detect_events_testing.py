from deepviewcore.Video import Video


videoPath = "C:/Users/migue/Documents/U/4to/TFG/DeepView/static/videos/Pez1.mp4"

v = Video(videoPath)
v.frame_interval = 30
events = []

def get_percentage(frame):
  return int(frame / v.numOfFrames() * 100)


def action(data):
  global events
  events.extend(data[1])
  print(f"Procesado {get_percentage(v.getCurrentFrameIndex())} %")


v.process(action=action, showContours=False, options = {
  "events": {"minArea": 200}
})


seconds = [v.getSecondForFrameIndex(e["frame_index"]) for e in events]
print("Se han detectado " + str(len(events)) + " eventos en los segundos " + str(seconds))


