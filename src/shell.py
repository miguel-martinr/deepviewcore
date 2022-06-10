
from Video import Video
import code
variables = globals().copy()
variables.update(locals())
shell = code.InteractiveConsole(variables)


# Video
path = "C:/Users/migue/Documents/U/4to/TFG/Videos/Pez1.mp4"
shell.push("from Video import Video")
shell.push(f"v = Video(\"{path}\")")



shell.interact()