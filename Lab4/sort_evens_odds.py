def sort_evens_odds(A):
    evenPos = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] % 2 == 0:
                if evenPos != i:
                    temp = A[evenPos]
                    A[evenPos] = A[i]
                    A[i] = temp
                    evenPos += 1
    # Sort to order the even part
    for i in range(evenPos):
        for j in range(i + 1, evenPos):
            if A[i] > A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    # Sort odd part
    for i in range(evenPos, len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
