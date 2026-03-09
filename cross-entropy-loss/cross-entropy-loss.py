import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    n = len(y_true)
    true_prob = y_pred[np.arange(n), y_true]

    loss = -np.log(true_prob)
    cross = np.mean(loss)

    return cross 