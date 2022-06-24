from deepviewcore.filters import preprocess


def preprocess_frame(frame):
    preprocessed = frame
    for meta in preprocess:
      filter = meta["filter"]
      options = meta["options"]
      preprocessed = filter(preprocessed, options)
      
    return preprocessed
