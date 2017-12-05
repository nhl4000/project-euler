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

sum = 2;
s = []
#for i in range(3,1000,2):
for i in range(1000000):
    s.append(isPrime(i))
    if isPrime(i) == 1:
        sum += i

#print(sum)
print(s)
