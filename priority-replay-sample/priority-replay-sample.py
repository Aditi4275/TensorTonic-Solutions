def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    n = len(priorities)
    power = [p**alpha for p in priorities]
    sum_power = sum(power)
    probs = [x/sum_power for x in power]

    raw_weight = [(n*pr)**(-beta) for pr in probs]

    max_raw = max(raw_weight)
    normalize = [w/max_raw for w in raw_weight]

    return [probs, normalize]