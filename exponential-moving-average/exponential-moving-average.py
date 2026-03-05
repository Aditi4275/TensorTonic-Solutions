def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    res = list(values)
    ans = []
    ans.append(res[0])
    
    for i in range(len(res)-1):
        k = alpha*res[i+1] + (1-alpha)*ans[i]
        ans.append(k)
        
    return ans