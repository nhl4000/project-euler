import math
def isPrime(n):
    if (n < 2):
        return 0;
    if (n % 2 == 0):
        return 0;
	
    for i in range(3, int(math.sqrt(n))+1,2):
        if (n % i == 0):
            return 0;
    return 1;

primeCount = 6
primeValue = 13
temp = 13;
while (primeCount != 10001):
    temp += 2
    if (isPrime(temp) == 1):
        primeCount += 1
        primeValue = temp

print(primeValue)
    
