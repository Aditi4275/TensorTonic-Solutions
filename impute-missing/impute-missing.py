import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    y = np.array(X, dtype=np.float64).copy()

    is1d = y.ndim == 1
    if is1d:
        y = y.reshape(-1,1)

    rows, cols = y.shape

    for j in range(cols):
        col = y[:, j]
        mask = np.isnan(col)
        observe = col[~mask]

        if observe.size == 0:
            fill = 0.0
        else:
            if strategy == 'mean':
                fill = np.mean(observe)
            elif strategy == 'median':
                fill = np.median(observe)
            else:
                raise ValueError
        
        y[mask, j] = fill
    return y.flatten() if is1d else y