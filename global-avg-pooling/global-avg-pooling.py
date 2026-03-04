import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    x = np.asarray(x)

    ndim = x.ndim
    if ndim == 3:
        spatial_axes = (1,2)
    elif ndim == 4:
        spatial_axes = (2,3)
    else:
        raise ValueError
        
    return np.mean(x, axis = spatial_axes)