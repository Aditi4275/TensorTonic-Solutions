import numpy as np 

def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    W = np.asarray(W)
    L = np.sqrt(6/(fan_in + fan_out))

    new_W = W * 2 * L - L
    return new_W