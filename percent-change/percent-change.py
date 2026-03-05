def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    res = list(series)
    ans = []
    for i in range(len(res)-1):
        if res[i] == 0:
             ans.append(0)
        else:
            change = (res[i+1] - res[i])/res[i]
            ans.append(change)

    return ans
    