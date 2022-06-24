from deepviewcore.filters import preprocess


def preprocess_frame(frame, options):
    preprocessed = frame
    print(options)
    for meta in preprocess:
        filter = meta["filter"]
        if options.get(meta["name"]) is None:            
            filter_options = meta["options"]
        else:          
            filter_options = options[meta["name"]]
            print(options)
        preprocessed = filter(preprocessed, filter_options)

    return preprocessed
