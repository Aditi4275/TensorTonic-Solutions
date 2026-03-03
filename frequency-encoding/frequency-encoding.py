def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    total_count = len(values)
    counts = {}
    
    for i in values:
        counts[i] = counts.get(i, 0)+1

    proportions = [counts[i] / total_count for i in values]

    return proportions