def partition_even_odd(A):
    evenPos = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            A[i], A[evenPos] = A[evenPos], A[i]
            evenPos += 1
    return A


A = [7, 17, 74, 21, 7, 9, 26, 10]
print(partition_even_odd(A))
