import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.asarray(x)
    mean = float(np.mean(x))
    median = float(np.median(x))
    mode_info = Counter(x.tolist()).most_common(1)
    mode_value = float(mode_info[0][0])
    
    return mean, median, mode_value