"""
    Suppose there are 3 matrices X, Y, Z with n*n dimentions
    X * Y = Z
"""
import numpy as np
import timeit

# Time complexity O(n^3)
def naive_method(X, Y):

    n = len(X)
    result = np.zeros((n, n), dtype="int64")
    for row in range(n):
        for col in range(n):
            for i in range(n):
                result[row][col] += X[row][i] * Y[i][col]
    return result
# #-----------------------------------------------------------------------
def split_matrix(matrix):
    """
        Split matrix into 4 submatrices
    """
    n = len(matrix)
    row, col = n//2, n//2
    return matrix[:row, :col],\
           matrix[:row, col:],\
           matrix[row:, :col],\
           matrix[row:, col:]

# time complexity: O(n^2)
def strassen(X, Y):

    if (len(X) == 1):
        return X * Y
    A, B, C, D = split_matrix(X)
    E, F, G, H = split_matrix(Y)

    p1 = strassen(A, F-H)
    p2 = strassen(A+B, H)
    p3 = strassen(C+D, E)
    p4 = strassen(D, G-E)
    p5 = strassen(A+D, E+H)
    p6 = strassen(B-D, G+H)
    p7 = strassen(A-C, E+F)

    c1 = p4 + p5 + p6 - p2
    c2 = p1 + p2
    c3 = p3 + p4
    c4 = p1 - p3 + p5 - p7

    result = np.vstack((np.hstack((c1, c2)), np.hstack((c3, c4))))

    return result
#-----------------------------------------------------------------------
n = 512
X = np.random.randint(1, 10, (n, n))
Y = np.random.randint(1, 10, (n, n))

print("naive method:")
start_time = timeit.default_timer()
naive_method(X, Y)
print(f"running time: {timeit.default_timer()-start_time}")
print("--------------")
print("strassen method:")
start_time = timeit.default_timer()
strassen(X, Y)
print(f"running time: {timeit.default_timer()-start_time}")



