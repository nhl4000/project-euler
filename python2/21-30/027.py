def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2): 
        if n%i==0:
            return False    
    return True

def primes_below(end):
    if end < 2:
        return []
    length = (end//2) - 1
    primes = [True]*length  
    for i in range(int(length**0.5)):  
        if primes[i]:
            for j in range(2*i*(i + 3) + 3, length, 2*i + 3):
                primes[j] = False  
    return [2] + [i*2 + 3 for i, j in enumerate(primes) if j]

primes = primes_below(1000)
longest = 0
for b in primes:
    for a in range(-999, 1000, 2):
        image = b
        n = 0
        while is_prime(image):
            n += 1
            image = n**2 + a*n + b
        if n > longest:
            longest = n
            result = a*b
print(result)
