def name_score(name):
    score = 0
    for i in name:
        score += ord(i) - 64
    return score

file_handler = open("p022_names.txt", "r")
names = list(eval(file_handler.read()))
file_handler.close()

names.sort()

result = 0
for i, name in enumerate(names):
    result += name_score(name)*(i+1)
print(result)
