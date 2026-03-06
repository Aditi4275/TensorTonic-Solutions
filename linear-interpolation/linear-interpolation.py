def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    ans = list(values)
    n = len(values)
    
    for i in range(n):
        if (ans[i] is None):
            left_index = i-1
            right_index = i
            
            while right_index < n and ans[right_index] is None:
                right_index += 1
                
            if left_index >= 0 and right_index < n:
                left_val = ans[left_index]
                right_val = ans[right_index]

                gap = right_index - left_index
                change = right_val - left_val

                for j in range(left_index+1, right_index):
                    ans[j] = left_val + (j - left_index) * change / gap
            
            i = right_index-1

    return ans