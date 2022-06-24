import cv2 as cv

def top_hat(frame, params):
    """Performs a top-hat operation on the given frame and returns the result."""
    # Getting the kernel to be used in Top-Hat
    filterSize = params["filterSize"]

    kernel = cv.getStructuringElement(cv.MORPH_RECT,
                                      filterSize)

    # Applying the Top-Hat operation
    filtered_frame = cv.morphologyEx(frame,
                                 cv.MORPH_TOPHAT,
                                 kernel)

    return filtered_frame

filter = {
  "name": "top_hat",
  "filter": top_hat,
  "options": {"filterSize": (9, 9)},
}

