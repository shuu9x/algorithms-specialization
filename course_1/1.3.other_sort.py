import timeit

def interchange_sort(arr):

    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if (arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

    return arr
#-------------------------------------------------------------
def selection_sort(arr):

    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            min_index = i
            if (arr[i] > arr[j]):
                min_index = j
        if (min_index != i):
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
#-------------------------------------------------------------
def bubble_sort(arr):

    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr
#-------------------------------------------------------------
def insertion_sort(arr):

    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        j = i
        while j > 0 and value < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = value

    return arr
#-------------------------------------------------------------
arr = [25, 30, 45, 6, 11, 90, 6, 25, 15]
print("interchange sort:")
start = timeit.default_timer()
interchange_sort(arr)
print(f"running time: {timeit.default_timer()-start}")

arr = [25, 30, 45, 6, 11, 90, 6, 25, 15]
print("selection sort:")
start = timeit.default_timer()
selection_sort(arr)
print(f"running time: {timeit.default_timer()-start}")

arr = [25, 30, 45, 6, 11, 90, 6, 25, 15]
print("bubble sort:")
start = timeit.default_timer()
bubble_sort(arr)
print(f"running time: {timeit.default_timer()-start}")

arr = [25, 30, 45, 6, 11, 90, 6, 25, 15]
print("insertion sort:")
start = timeit.default_timer()
insertion_sort(arr)
print(f"running time: {timeit.default_timer()-start}")