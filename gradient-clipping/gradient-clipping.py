import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g = np.asarray(g)
    x = g.copy()

    modx = np.linalg.norm(x)
    
    if (modx <= max_norm) or (max_norm <= 0):
        return g
    else:
        return (g * max_norm)/modx