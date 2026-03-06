def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    ans = []

    for i in range(len(values)-len(weights)+1):
        context = values[i : i+len(weights)]
        mean = 0
        for j in range(len(weights)):
            mean += (context[j] * weights[j])
        ele = mean/sum(weights)
        ans.append(ele)

    return ans