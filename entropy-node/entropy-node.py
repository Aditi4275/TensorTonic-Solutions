import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    y = np.asarray(y)
    
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    prob = counts/len(y)
    entropy = -np.sum(prob*np.log2(prob))
    
    return float(np.abs(entropy))