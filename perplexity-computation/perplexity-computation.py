import numpy as np 

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    prob = np.asarray(prob_distributions)
    tokens = np.asarray(actual_tokens)

    n = len(tokens)
    if n == 0:
        return 0.0

    actual_probs = prob[np.arange(n), tokens]
    log_prob = np.log(actual_probs)
    cross_entropy = -np.sum(log_prob)/n
    pp = np.exp(cross_entropy)

    return float(pp)