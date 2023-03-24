def oddodd_eveneven(A):
    evenPos = 0
    oddPos = 1
    t = A[0]

    for i in range(len(A)):
        if A[i] % 2 == 0 and i % 2 == 0:  # Number even, position even
            evenPos += 1
        elif A[i] % 2 != 0 and i % 2 != 0:  # Number odd, position odd
            oddPos += 1
        elif A[i] % 2 == 0 and i % 2 != 0:  # Number even, position odd
            t = A[evenPos]
            A[evenPos] = A[i]


A = [50, 47, 92, 78, 76, 7, 60, 36, 59, 30, 50, 43]

A = [47, 50, 7, 78, 59, 76, 43, 92, 36, 60, 30, 50]

print(A)
print(oddodd_eveneven(A))

