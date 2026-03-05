import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    X = np.asarray(X)
    if X.ndim != 2:
        return None
        
    n = X.shape[0]
    if n < 2:
        return None
        
    feature_mean = np.mean(X, axis=0, keepdims=True)
    centered = X - feature_mean
    cov = (centered.T @ centered)/(n-1)

    std = np.std(X, axis=0, ddof=1)
    den = np.outer(std.T , std)

    corr = np.divide(cov, den, out=np.full_like(cov, np.nan), where=den!=0)
    np.fill_diagonal(corr, np.where(std != 0, 1.0, np.nan))

    return corr
    
    