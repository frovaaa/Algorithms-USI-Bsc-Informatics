def sort(A, n):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if n == 0:
                if A[i] < A[j]:
                    temp = A[i]
                    A[i] = A[j]
                    A[j] = temp
            elif n == 1:
                if A[i] > A[j]:
                    temp = A[i]
                    A[i] = A[j]
                    A[j] = temp
