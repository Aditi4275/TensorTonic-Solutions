def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    ans = []
    
    for i in range(len(values)-window_size+1):
        context = values[i : i+window_size]
        context = sorted(context)

        if window_size%2 == 0:
            k = (context[window_size//2-1] + context[window_size//2])/2
            ans.append(k)
        else:
            k = context[window_size//2]
            ans.append(k)

    return ans