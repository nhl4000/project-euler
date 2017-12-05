def factorial(n):
    sum = 1
    for i in xrange(1,n+1):
        sum *= i
    return sum

def binomial_coefficient(n, k):
    num = factorial(n)
    dem = factorial(k) * factorial(n-k)
    return num / dem

n = 20
k = 20
print (binomial_coefficient(n+k,k))
    
