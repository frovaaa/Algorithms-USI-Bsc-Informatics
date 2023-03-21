def sieve_of_erathosthenes(n):
    result = []
    
    P = [True]*(n+1) #create an array of n+1 values all value=True
    P[0] = False
    P[1] = False
    i=2
    while i * i < len(P):
        # i is our initial prime
        if P[i] == True:
            # cross out all multiple of i
            j = i * i
            while j < len(P):
                P[j]=False
                j = j + i
        i = i + 1

    for k in range(len(P)):
        if P[k]:
            result.append(k)
    return result

def prime_factorize(n):
    resultString = ""
    primes = sieve_of_erathosthenes(n)
    result = 1
    finalResult = ""

    #Search for first prime that is divisor
    for i in range((len(primes) - 1), -1, -1):
        if(n % primes[i] != 0):
            continue
    
        result = primes[i]
        power = 1
        
        #Get biggest 
        while n % pow(primes[i], power + 1) == 0:
            power += 1
        
        if power == 1:
            finalResult = str(result) + " " + finalResult
        else:
            finalResult = str(result) +  "E" + str(power) + " " + finalResult
        n = n // pow(result, power)

    return finalResult[0 : len(finalResult) - 1]



# print(prime_factorize(10242311))