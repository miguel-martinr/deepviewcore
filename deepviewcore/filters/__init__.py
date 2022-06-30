# Filters to be applied to image, in the same order
from deepviewcore.filters import top_hat
from deepviewcore.filters import denoise
from deepviewcore.filters import to_gray
from deepviewcore.filters import threshold

# Filtros a aplicar sobre cada frame
preprocess = [
    # Pasar a escala de grises
    to_gray.filter,

    # Homogeneizar fondo
    top_hat.filter,

    # Quitar ruido
    denoise.filter,  # Actualmente no hace nada  
]


process = [
    threshold.filter
]







