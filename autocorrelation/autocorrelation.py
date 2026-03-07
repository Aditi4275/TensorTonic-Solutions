import numpy as np 

def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    s = np.asarray(series, dtype=np.float64)
    mean = np.mean(s)
    variance = np.sum((s - mean)**2)
    n = len(s)
    
    if variance == 0:
        return [1.0] + [0.0] * max_lag
    
    centered_s = s - mean
    acf = []

    for i in range(max_lag + 1):
        if i == 0:
            acf.append(1.0)
            continue 

        num = np.sum(centered_s[:n-i] * centered_s[i:])

        acf.append(num/variance)

    return acf