import numpy as np 

def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    values = np.asarray(values)
    min_val = np.min(values)
    max_val = np.max(values)

    if min_val == max_val:
        return np.zeros_like(values, dtype=int).tolist()

    bin_width = (max_val - min_val)/num_bins
    
    bin_indices = ((values - min_val)/bin_width).astype(int)

    bin_indices = np.clip(bin_indices, 0, num_bins-1)
    
    return bin_indices.tolist()