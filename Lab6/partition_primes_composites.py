def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, n // 2, 2):
        if n % i == 0:
            return False
    return True

def partition_primes_composites(A):
    primePos = 0
    for i in range(len(A)):
        if isPrime(A[i]):
            A[i], A[primePos] = A[primePos], A[i]
            primePos += 1
    return A

# Complexity = O(n^2)
# O(n) to scan all the array
# for each element I do O(n) to check if it's prime

# A = [7, 17, 74, 21, 7, 9, 26, 10, 11, 449, 52, 47, 7, 3, 5]
# print(partition_primes_composites(A))
