def minAndMax(A):
    if(len(A) == 0):
        return "Error Array Empty"
    
    tempMax = A[0]
    tempMin = A[0]
    for i in range(1, len(A)):
        if (A[i] < tempMin):
            tempMin = A[i]
        if (A[i] > tempMax):
            tempMax = A[i]
    return "Min: ",tempMin," Max: ",tempMax

# print(minAndMax([1,2,3]))
# print(minAndMax([1, 10, 20, 30, -1, 40, 50]))