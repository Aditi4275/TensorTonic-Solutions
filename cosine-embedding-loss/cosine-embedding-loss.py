import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    x1 = np.asarray(x1, dtype=float)
    x2 = np.asarray(x2, dtype=float)
    
    num = np.dot(x1, x2)
    
    den1 = np.linalg.norm(x1)
    den2 = np.linalg.norm(x2)
    
    cos = num/(den1*den2)

    if label == 1:
        return 1 - cos
    else:
        return np.maximum(0, cos-margin)
    
