import numpy as np
def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    image = np.asarray(image, dtype=float)
    weights = np.array([0.299, 0.587, 0.114])
    
    grayscale = image @ weights

    return grayscale.tolist()