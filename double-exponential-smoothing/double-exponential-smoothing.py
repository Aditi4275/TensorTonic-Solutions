def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    l = []
    l.append(series[0])
    b = []
    b.append(series[1] - series[0])
    
    for i in range(1, len(series)):
        l1 = alpha*series[i] + (1-alpha)*(l[i-1] + b[i-1])
        b1 = beta*(l1 - l[i-1]) + (1-beta)* (b[i-1])

        l.append(l1)
        b.append(b1)

    return l
    