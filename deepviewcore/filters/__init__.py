# Filters to be applied to image, in the same order
from deepviewcore.filters.top_hat import top_hat
from deepviewcore.filters.denoise import denoise
from deepviewcore.filters.to_gray import to_gray

# Filtros a aplicar sobre cada frame
preprocess = [
    # Homogeneizar fondo
    {"filter": top_hat, "options": {"filterSize": (9, 9)}, "name": "top_hat"},

    # Pasar a escala de grises
    {"filter": to_gray, "options": None, "name": "to_gray"},

    # Quitar ruido
    {"filter": denoise, "options": None, "name": "denoise"}  # Actualmente no hace nada  
]
