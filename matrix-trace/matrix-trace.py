import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.asarray(A)
    ans = 0
    
    for i in range(A.shape[0]):
        ans += A[i][i]

    return float(ans)
