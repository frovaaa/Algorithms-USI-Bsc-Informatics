def is_monotonic(A, i, j):
        increasing = True
        decreasing = True
        for k in range(i, j):
            if A[k] < A[k + 1]:
                  decreasing = False
            elif A[k] > A[k + 1]:
                  increasing = False
            if increasing == False and decreasing == False:
                  return False
        return True

print(is_monotonic([1,2,3], 0, 2))
print(is_monotonic([1,1,7,7,9], 0, 4))
print(is_monotonic([9,9,5], 0, 2))
print(is_monotonic([6,6,6,6,6,6], 2, 4))
print(is_monotonic([1,1,1,2,1,3], 0, 5))
print(is_monotonic([1,1,1,2,1,3], 0, 3))
print(is_monotonic([3,2,1,3,2,1], 0, 5))
print(is_monotonic([3,2,1,3,2,1], 2, 3))
print(is_monotonic([3,2,1,3,2,1], 2, 4))
print(is_monotonic([3,2,1,3,2,1], 3, 5))
print(is_monotonic([7,4,7], 0, 2))
print(is_monotonic([7,4,7], 1, 2))