def oddodd_eveneven(A):
    nOfEvens = 0
    nOfOdds = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            nOfEvens += 1
        else:
            nOfOdds += 1

    if nOfEvens >= nOfOdds:
        howManyRem = nOfEvens - (len(A) // 2)

        evenPos = 0
        for k in range(0, len(A), 1):
            if evenPos >= len(A):
                break

            if A[evenPos] % 2 == 0:
                evenPos += 2

            if k % 2 == 0 and k >= evenPos:
                if A[k] % 2 == 0:
                    A[k], A[evenPos] = A[evenPos], A[k]
                    evenPos += 2
            elif k % 2 != 0:
                if A[k] % 2 == 0:
                    A[k], A[evenPos] = A[evenPos], A[k]
                    evenPos += 2

        finalPos = 0
        if (len(A) - 1) % 2 == 0:
            finalPos = len(A) - 2
        else:
            finalPos = len(A) - 1

        for j in range(1, len(A), 2):
            if howManyRem == 0:
                break

            if A[j] % 2 == 0:
                A[j], A[finalPos] = A[finalPos], A[j]
                finalPos -= 2
                howManyRem -= 1
    else:
        howManyRem = nOfEvens - (len(A) // 2)

        oddPos = 1
        for k in range(0, len(A), 1):
            if oddPos >= len(A):
                break

            if A[oddPos] % 2 != 0:
                oddPos += 2

            if k % 2 != 0 and k >= oddPos:
                if A[k] % 2 != 0:
                    A[k], A[oddPos] = A[oddPos], A[k]
                    oddPos += 2
            elif k % 2 != 0:
                if A[k] % 2 != 0:
                    A[k], A[oddPos] = A[oddPos], A[k]
                    oddPos += 2

        finalPos = 0
        if (len(A) - 1) % 2 == 0:
            finalPos = len(A) - 2
        else:
            finalPos = len(A) - 1

        for j in range(1, len(A), 2):
            if howManyRem == 0:
                break

            if A[j] % 2 == 0:
                A[j], A[finalPos] = A[finalPos], A[j]
                finalPos -= 2
                howManyRem -= 1

    return A


# A = [17, 18, 18, 10, 6, 4, 60, 37, 59, 31, 42, 43]
# A = [17, 18, 18, 11, 3, 5, 60, 37, 59, 31, 47, 43]
A = [17, 12, 18, 10, 6, 5, 60, 36, 59, 32, 42, 43]

# A = [47, 50, 7, 78, 59, 76, 43, 92, 36, 60, 30, 50]

print(A)
print(oddodd_eveneven(A))

