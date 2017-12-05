for m in range(1001):
    for n in range(m):
        a = (m*m) - (n*n)
        b = 2*m*n
        c = (m*m) + (n*n)

        if (a+b+c == 1000):
            print(a*b*c)
