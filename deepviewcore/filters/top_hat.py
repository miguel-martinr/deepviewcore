import cv2 as cv


def top_hat(frame, options):
    """Performs a top-hat operation on the given frame and returns the result."""
    # Getting the kernel to be used in Top-Hat

    filterSize = options["filterSize"]
    se = options["se"]

    kernel = cv.getStructuringElement(se,
                                      filterSize)

    # Applying the Top-Hat operation
    filtered_frame = cv.morphologyEx(frame,
                                     cv.MORPH_TOPHAT,
                                     kernel)

    return filtered_frame


filter = {
    "name": "top_hat",
    "filter": top_hat,
    "options": {"filterSize": (9, 9), "se": cv.MORPH_ELLIPSE},
}
