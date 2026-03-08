import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    p = np.asarray(p).flatten()
    y = np.asarray(y).flatten()

    py = np.sum(p * y)
    num = 2 * py + eps
    den = np.sum(p) + np.sum(y) + eps

    return 1 - num/den