def divisors(nb, ext = False):
    divisors = []
    for i in range(2, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb//i)
    return divisors

def d(nb):
    return 1 + sum(divisors(nb))

result = 0
for a in range(1, 10000):
    b = d(a)
    if d(b) == a and a != b:
        result += a
print(result)
