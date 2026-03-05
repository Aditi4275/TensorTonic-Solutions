import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.asarray(X)
    if X.ndim != 2:
        return None
        
    n = X.shape[0]
    if n < 2:
        return None
        
    feature_means = np.mean(X, axis = 0, keepdims=True)

    center = (X - feature_means)
    
    centerT = center.T

    matrix = (centerT @ center)/(n-1)

    return matrix