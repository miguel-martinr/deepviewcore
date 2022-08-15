from deepviewcore.Video import Video


videoPath = "C:/Users/migue/Documents/U/4to/TFG/DeepView/static/videos/Pez1.mp4"

v = Video(videoPath)

action = lambda data: print(data)
v.process(action=action, showContours=True)