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

number = 600851475143;
highest_prime = 3;
for i in range(3, int(math.sqrt(number)), 2):
    if isPrime(i) == 1 and (number % i == 0):
        highest_prime = i

print(highest_prime)
