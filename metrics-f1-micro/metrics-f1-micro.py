import numpy as np 

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    if y_true.size == 0:
        return 0.0
        
    tp = np.sum(y_true == y_pred)
    total = y_true.size
    fp = total - tp
    fn = total - tp

    f1 = 2*tp/(2*tp + fp + fn)

    return float(f1)