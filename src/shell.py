
from json import JSONEncoder
from Video import Video
import code

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


variables = globals().copy()
variables.update(locals())
shell = code.InteractiveConsole(variables)


# Video
path = "C:/Users/migue/Documents/U/4to/TFG/Videos/Pez1.mp4"
shell.push("from Video import Video")
shell.push(f"v = Video(\"{path}\")")



shell.interact()