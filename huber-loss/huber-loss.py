import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    error = np.abs(y_true - y_pred)

    e1 = (error**2)*0.5
    e2 = delta* (error - (delta*0.5))
    loss = np.where(error>delta, e2, e1)
    
    return float(np.mean(loss))