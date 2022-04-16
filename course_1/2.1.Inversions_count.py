"""
- Input: array A containing the numbers 1, 2, 3,..., n in some arbitrary
order.
- Output: number of inversions = number of pairs (i, j) of array indices
with i < j and A[i] > A[j]
"""
import timeit
import random

def inversions_brute_force(arr):
    n = len(arr)
    inversion_count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (arr[i] > arr[j]):
                inversion_count += 1
    return inversion_count
#-----------------------------------------------------------------------
def merge_array(left_arr, right_arr, left_array_length):

    i, j, n = 0, 0, len(left_arr) + len(right_arr)
    global count
    result = []
    for index in range(n):
        try:
            if (left_arr[i] <= right_arr[j]):
                result.append(left_arr[i])
                i += 1
            else:
                result.append(right_arr[j])
                count += (left_array_length - i)
                j += 1
        except IndexError as idxErr:
            if i > len(left_arr) - 1:
                result += right_arr[j:]
                break
            else:
                result += left_arr[i:]
                break
    return result

def inversions_merge_sort(arr):

    if len(arr) == 1:
        return arr

    half_len = len(arr) // 2
    # sorting subarrays
    left_arr = inversions_merge_sort(arr[:half_len])
    right_arr = inversions_merge_sort(arr[half_len:])

    left_array_length = len(left_arr)
    result = merge_array(left_arr, right_arr, left_array_length)
    return result
#-----------------------------------------------------------------------
random.seed(1)
arr1 = [random.randint(1, 100) for _ in range(10000)]
# Time complexity O(n^2)
start_brute_force = timeit.default_timer()
result = inversions_brute_force(arr1)
end_brute_force = timeit.default_timer()
print(f"using brute force: {result}")
print(f"running time: {end_brute_force - start_brute_force}")
#-----------------------------------------------------------------------
random.seed(1)
arr2 = [random.randint(1, 100) for _ in range(10000)]
# Time complexity O(nlog(n))
count = 0
start_merge_sort = timeit.default_timer()
inversions_merge_sort(arr2)
end_merge_sort = timeit.default_timer()

print(f"using merge sort: {count}")
print(f"running time: {end_merge_sort - start_merge_sort}")
