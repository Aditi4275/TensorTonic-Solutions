import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x= np.asarray(x)
    mean= np.mean(x)
    deviation = x - mean
    n = x.shape[0]

    variance = np.sum(deviation**2)/(n-1)
    std = np.sqrt(variance)
    return variance, std