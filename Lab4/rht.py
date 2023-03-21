def rht(A, n):
    result = []
    i = 0
    while i < len(A):
        count = 0
        finding = A[i]
        j = 0
        while j < len(A):
            if A[j] == finding:
                count += 1
                A = A[j + 1:]
            else:
                j += 1
        if count <= n:
            for k in range(count):
                result.append(finding)
    return result
