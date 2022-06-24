from deepviewcore.filters import preprocess


def preprocess_frame(frame, options):
    preprocessed = frame
    for meta in preprocess:
        filter = meta["filter"]
        
        # Add default options
        default_options = meta["options"] 
        filter_options = {}

        if (default_options is not None):
          filter_options.update(default_options)
        
        specific_options = options.get(meta["name"])

        if specific_options is not None:                                
            # Merge default and specific options
            filter_options.update(specific_options) 
                                   
        print(f"###OPTIONS: ")
        print(filter_options)
        preprocessed = filter(preprocessed, filter_options)

    return preprocessed
