dimension = 1001
result = 1
n = 1
for k in range(2, dimension, 2):
    for j in range(4):
        n += k
        result += n
print(result)
