def partition_even_odd(A):
    evenPos = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            temp = A[i]
            A[i] = A[evenPos]
            A[evenPos] = temp
            evenPos += 1


A = [-1, 1, 7, 5, -2, 1, 2, 7, 7, 5, 5, 1, 6, 4, 4]
partition_even_odd(A)
print(A)
