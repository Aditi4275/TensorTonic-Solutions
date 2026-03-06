def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    ans = []

    for i in range(len(values)-window_size+1):
        context = values[i : i+window_size]
        mean = sum(context)/window_size
        ans.append(mean)

    return ans