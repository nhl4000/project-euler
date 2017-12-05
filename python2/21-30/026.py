def cycle_length(den):
    n = 10
    i = 0
    while n != 10 or i < 1:
        n = (n % den) * 10
        i += 1
    return i

longest = 0
for i in range(2, 1000):
    if i%2 != 0 and i%5 != 0:
        length = cycle_length(i)
        if length > longest:
            longest = length
            result = i
print(result)
