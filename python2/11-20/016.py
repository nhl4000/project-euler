import math

d = int(math.pow(2,1000))
s = str(d)
sum = 0
for c in s:
    sum += int(c)

print(sum)
