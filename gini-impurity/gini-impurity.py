import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    y_left = np.asarray(y_left)
    y_right = np.asarray(y_right)

    nl = len(y_left)
    nr = len(y_right)
    n = nl + nr

    if n == 0:
        return 0.0

    def calculate_gini(y, count):
        if count == 0:
            return 0.0
        _, counts = np.unique(y, return_counts=True)
        probs = counts/ count
        return 1 - np.sum(probs**2)
   

    gini_lf = calculate_gini(y_left, nl)
    gini_rg = calculate_gini(y_right, nr)


    gini = ((nl * gini_lf)/n) + ((nr * gini_rg) / n)

    return gini