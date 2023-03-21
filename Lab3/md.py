def md(A):
    result = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            tempResult = abs(A[i] - A[j])
            if tempResult > result:
                result = tempResult
    return result