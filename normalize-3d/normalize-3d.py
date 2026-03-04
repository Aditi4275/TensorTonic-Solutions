import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.asarray(v)
    norms = np.linalg.norm(v, axis = -1, keepdims=True)
    eps = 1e-12
    return np.where(norms>eps, v/norms, 0.0)