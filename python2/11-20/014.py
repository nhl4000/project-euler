def collatz_sequence_length(n,length=0):
    length += 1
    while (n != 1):
        if (n % 2 == 0):
            n = n / 2
        else:
            n = (3*n) + 1
        length += 1  
    return length

greatest = 0
greatestStart = 0
for i in xrange(1,1000000):
    temp = collatz_sequence_length(i)
    if temp > greatest:
        greatest = temp
        greatestStart = i
        print([i, greatest])

print(greatestStart)
