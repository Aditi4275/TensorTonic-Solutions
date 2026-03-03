import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    x = np.asarray(x, dtype = float)
    s1 = lam * x
    s2 = lam * alpha * (np.exp(x) -1)

    loss = np.where(x>0, s1, s2)
    return np.round(loss, 4).tolist()
    
