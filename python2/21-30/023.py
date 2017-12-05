def divisors(nb):
    divisors = []
    for i in range(2, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb//i)
    return divisors

def is_abundant(n):
    return sum(divisors(n))+1 > n

abundants = [i for i in range(2, 28124) if is_abundant(i)]
sums = {}
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        num = abundants[i] + abundants[j]
        if num > 28123:
            break
        sums[num] = 1
        
result = (28123*28124)//2 - sum(sums.keys())
print(result)
