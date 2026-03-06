import math  

def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    ans = []

    for i in range(len(values) - window_size + 1):
        context = values[i : i+window_size]
        mean = sum(context)/window_size
        var = 0
        
        for j in range(window_size):
            var += (context[j] - mean)**2

        var = var/window_size
        ans.append(math.sqrt(var))
    return ans