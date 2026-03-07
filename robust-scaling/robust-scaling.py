def get_median(data):
    n = len(data)
    if n == 0:
        return 0
    mid = n // 2
    if n%2 == 0:
        return (data[mid-1]+data[mid])/2
    else:
        return data[mid]
        
def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    if not values: return []
    sort_values = sorted(values)
    
    median =get_median(sort_values)
    n = len(sort_values)
    
    mid = n // 2
    
    if n % 2 == 0:
        lf = sort_values[: mid]
        hf = sort_values[mid: ]
    else:
        lf = sort_values[: mid]
        hf = sort_values[mid+1: ]

    q1 = get_median(lf)
    q3 = get_median(hf)

    iqr = q3 - q1
    if iqr == 0:
        return [0.0 for _ in values]

    return [(x - median)/iqr for x in values]