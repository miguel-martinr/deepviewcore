from deepviewcore.filters import process


def process_frame(frame, options):
    processed = frame
    for meta in process:
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
                                           
        processed = filter(processed, filter_options)

    return processed