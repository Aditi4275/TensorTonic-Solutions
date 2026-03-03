import numpy as np

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    x = np.asarray(x)
    n = alpha * (np.exp(x)-1)

    elu = np.where(x>0, x, n)

    return elu.tolist()