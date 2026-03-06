import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    pred = np.asarray(predictions)
    num_samples = pred.shape[1]

    final_pred = []

    for i in range(num_samples):
        votes = pred[:, i]
        counts = np.bincount(votes)
        max_votes = np.max(counts)

        winners = np.where(counts == max_votes)[0]
        final_pred.append(int(winners[0]))
        
    return final_pred