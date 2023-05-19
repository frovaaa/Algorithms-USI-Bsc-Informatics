def BetterAlgoX(A):
    j = 0
    for i in range(len(A)):
        if A[i] % 2 != 0:
            A[i], A[j] = A[j], A[i]
            j = j+1
    return j
