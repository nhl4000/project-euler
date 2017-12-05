import math

highest = 0

for count in range(100,1000):
    for count2 in range(100,1000):
        sum = count * count2
        size = int(math.log10(sum))+1
        a = str(sum)
        bFailed = 0

        for index in range(0, int(size / 2) + 1):
            if a[index] == a[size - 1 - index]:
                continue;
            else:
                bFailed = 1
        
        if bFailed == 0:
            if (highest < sum):
                highest = sum
        
print(highest);
