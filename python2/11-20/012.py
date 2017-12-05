import math

def triangle_number(n):
    return (n * (n+1)) / 2

def num_of_factors(n):
    count = 1
    for counter in xrange(1, int(math.sqrt(n))+1):
        if ((n % counter) == 0):
            count += 2
    return count

count = 0
i = 1

while(count <= 500):
    tn = triangle_number(i)
    temp = num_of_factors(tn)
    if temp > count:
        count = temp
        print([i, count])
    i += 1

print(triangle_number(i-1))


