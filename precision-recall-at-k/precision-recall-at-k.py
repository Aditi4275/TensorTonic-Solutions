import numpy as np

def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    top_k = np.asarray(recommended[:k])
    relevant = np.asarray(relevant)
    intersection = np.isin(top_k, relevant)

    precision = np.sum(intersection)/k
    recall = np.sum(intersection)/len(relevant)

    return list([precision, recall])