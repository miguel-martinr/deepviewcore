from deepviewcore.Video import Video


videoPath = "C:/Users/migue/Documents/U/4to/TFG/DeepView/static/videos/Pez1.mp4"

v = Video(videoPath)

events = {}

def action(data):
  global events
  events.update(data[1])

v.process(action=action, showContours=False)

print("Se han detectado" + str(len(events)) + "eventos en los segundos: " + str(events.keys()))


