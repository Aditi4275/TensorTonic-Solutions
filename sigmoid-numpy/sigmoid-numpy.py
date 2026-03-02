import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x)
    s = 1/(1+np.exp(-x))
    return s
    pass