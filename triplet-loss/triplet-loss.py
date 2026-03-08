import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    anchor = np.atleast_2d(anchor)
    positive = np.atleast_2d(positive)
    negative = np.atleast_2d(negative)

    dap = np.sum((anchor - positive)**2, axis=1)
    dan = np.sum((anchor - negative)**2, axis=1)

    l = np.maximum(0, dap - dan + margin)

    return np.mean(l)