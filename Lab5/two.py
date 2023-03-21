def is_sorted(A):
    asc = True
    desc = True
    for i in range(1, len(A)):
        if (A[i - 1] < A[i]) and (not asc) or (A[i - 1] > A[i]) and (not desc):
            return False
        elif A[i - 1] < A[i]:
            desc = False
        elif A[i - 1] > A[i]:
            asc = False
    return True
