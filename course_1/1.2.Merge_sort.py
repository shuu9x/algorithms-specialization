"""
    - Suppose the unsorted array has n elements.
    - Because we divide array into 2 subarrays, so there are log2(n) + 1
    recursion tree levels.
    - At level i: there are 2^i subproblems, each of size n/(2^i).
    Total operation at level i = 2^i * x*[n/(2^i)] = x*n (where x is
    the number of operations in each loop to merge 2 subarrays)
    => T(n) = x*n*[log2(n) + 1] = x*n*log2(n) + x*n
    - Time complexity: O(nlog2(n))
"""
def merge_array(left_arr, right_arr):
    """merge 2 subarrays in ascending order
    Args:
        left_arr (list): first half array
        right_arr (list): second half array
    Returns:
        list: list of sorted array after merge 2 subarrays
    """
    i, j, n = 0, 0, len(left_arr) + len(right_arr)
    result = []
    for index in range(n):
        try:
            if (left_arr[i] <= right_arr[j]):
                result.append(left_arr[i])
                i += 1
            else:
                result.append(right_arr[j])
                j += 1
        except IndexError as idxErr:
            if i > len(left_arr) - 1:
                result += right_arr[j:]
                break
            else:
                result += left_arr[i:]
                break
    return result

def merge_sort(arr):
    """merge sort implementation
    Args:
        arr (list): unsorted list
    Returns:
        list: sorted list
    """
    if len(arr) == 1:
        return arr

    half_len = len(arr) // 2
    # seperate array into 2 subarrays
    left_arr = arr[:half_len]
    right_arr = arr[half_len:]
    # sorting subarrays
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    result = merge_array(left_arr, right_arr)
    return result

arr = [25, 30, 45, 6, 11, 90, 15]
print(merge_sort(arr))