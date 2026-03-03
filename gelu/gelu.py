import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    x = np.asarray(x)
    v = np.vectorize(math.erf)
    
    f = (1 + v(x/np.sqrt(2)))/2
    return f*x.astype(float)
                         
