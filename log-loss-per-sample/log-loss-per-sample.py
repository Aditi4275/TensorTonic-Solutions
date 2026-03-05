import math
import numpy as np
def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    
    p = np.clip(y_pred, eps, 1-eps)
    l = -(y_true*np.log(p) + (1-y_true)*np.log(1-p)).astype(float)

    return l.tolist()
        