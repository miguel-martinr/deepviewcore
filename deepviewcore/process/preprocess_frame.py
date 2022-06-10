from .filters.top_hat import top_hat
import cv2 as cv

default_options = {
    "filter": top_hat,
    "filter_params": {
        "filterSize": (9, 9),
    }
}


def homogeneize_background(frame, options = default_options):
    filter = options["filter"]
    filter_params = options["filter_params"]
    return filter(frame, filter_params)


def frame_to_gray(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    return gray


def denoise(frame):
    return frame


def preprocess_frame(frame):
    homogeneized = homogeneize_background(frame)
    gray = frame_to_gray(homogeneized)
    denoised = denoise(gray)
    return denoised
