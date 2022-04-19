import random

def partition_left_pivot(arr, left, right):

    pivot = arr[left]
    i = left + 1
    for j in range(left+1, right+1):
        if (arr[j] <= pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[left], arr[i-1] = arr[i-1], arr[left]

    return i-1

def partition_right_pivot(arr, left, right):

    pivot = arr[right]
    i = left
    for j in range(left, right):
        if (arr[j] <= pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[right], arr[i] = arr[i], arr[right]
    return i

def partition_middle_pivot(arr, left, right):

    pivot = arr[(left+right) // 2]
    i, j = left, right
    while True:
        while arr[i] < pivot:
            i = i + 1
        while arr[j] > pivot:
            j = j - 1
        if (i >= j):
            return j
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1

def quick_sort(arr, left, right):

    if arr and left < right:
        mid = partition_left_pivot(arr, left, right)
        # mid = partition_right_pivot(arr, left, right)
        # mid = partition_middle_pivot(arr, left, right)
        quick_sort(arr, left, mid-1)
        quick_sort(arr, mid+1, right)
        # using 2 recursive calls below incase middle pivot
        # quick_sort(arr, left, mid)
        # quick_sort(arr, mid+1, right)
#-----------------------------------------------------------------------
def test(n, testcase):
    """quick sort test

    Args:
        n (int): number of elements in test list
        testcase (int): number of test cases
    """
    for i in range(testcase):
        lst = [random.randint(1, 31) for i in range(n)]
        print(f"case {i+1}: {lst}.", end=' ')
        quick_sort(lst, 0, n-1)
        result = "Passed!" if sorted(lst) == lst else "Failed!"
        print(result)

test(8, 10)
