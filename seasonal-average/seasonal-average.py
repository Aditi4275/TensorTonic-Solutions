def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    ans = []
    i = 0
    while i < period:
        p = i
        k = 0
        count = 0
        for p in range(p, len(series), period):
            k = k + series[p]
            count += 1
            
        k = k/count
        ans.append(k)
        i += 1

    return ans