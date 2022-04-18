"""
file: IntegerArray.txt
This file contains all of the 100,000 integers between 1 and 100,000
(inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given,
where the i row of the file indicates the i entry
of an array.

Because of the large size of this array, you should implement the fast
divide-and-conquer algorithm covered in the video lectures.
"""
import timeit
import os
import sys

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

def load_data():

    file_path = os.path.join(os.path.dirname(sys.argv[0]), 'IntegerArray.txt')
    with open(file_path, "r") as file:
        data = file.read().split('\n')
    return list(map(int, data))

if __name__ == '__main__':
    data = load_data()
    count = 0
    start = timeit.default_timer()
    inversions_merge_sort(data)
    stop = timeit.default_timer()
    print(f"number of inversions: {count}")
    print(f"running time: {stop-start}")
