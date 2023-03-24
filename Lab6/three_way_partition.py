def three_way_partition(A, v):
    p = 0
    posEl = -1

    #Find v
    for i in range(len(A)):
        if A[i] == v:
            posEl = i
            break
    if posEl == -1:
        return posEl

    A[posEl], A[len(A) - 1] = A[len(A) - 1], A[posEl]
    for k in range(len(A)):
        if A[k] < v:
            A[k], A[p] = A[p], A[k]
            p += 1

    # p -= 1
    q = p

    for j in range(p, len(A)):
        if A[j] == v:
            A[j], A[q] = A[q], A[j]
            q += 1

    return "P: ", p, " Q: ", q

A = [15, 5, 12, 5, 123, 54, 32, 12, 12, 7, 2]
print(three_way_partition(A, 12))
print(A)