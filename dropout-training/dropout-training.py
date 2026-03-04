import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    x = np.asarray(x, dtype=float)
    if rng is None:
        rng = np.random.default_rng()

    mask = rng.random(x.shape)
    scale = 1.0 / (1.0 - p)
    pattern = np.where(mask < (1-p), scale, 0.0)
    out = x * pattern
    
    return out, pattern