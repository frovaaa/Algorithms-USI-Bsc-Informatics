def rotate(A, k):
    if k == len(A):
        return A

    B = A[k:len(A)]
    C = A[:k]
    result = B + C
    return result

# def rotate_in_place(A,k):
#     for i in range(len(A) + k):
#         realI = (i - k) % len(A)
#
#         temp = A[i]
#         A[i] = A[realI]
#         A[realI] = temp
#     return A

# # print(rotate([1,2,3,4,5,6,7,8,9],10))
# #[2,3,4,5,6,7,8,9,1]
# print(rotate_in_place([1,2,3,4,5,6,7,8,9],10))

# def rotate_in_place(A,k):
#     for i in range(k):
#         A.append(A[0])
#         del A[0]
#     return A

def rotate_in_place(A, k):
    flip(A, 0, len(A) - k)
    flip(A, 0, len(A))
    return A


def flip(A, begin, end):
    for i in range(begin, end // 2):
        A[i], A[end - i - 1] = A[end - i - 1], A[i]

