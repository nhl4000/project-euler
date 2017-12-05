smallest = 20
bFailed = 1
while(bFailed == 1):
    bFailed = 0
    for counter in range(1,21):
        if smallest % counter != 0:
            bFailed = 1
            break

    smallest += 20


print(smallest-20)
