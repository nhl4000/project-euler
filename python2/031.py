coins = [1, 2, 5, 10, 20, 50, 100, 200]
# n is the amount, i is the index of the highest denomination used to sum up to n
def ways(n, i):
	if i == 0:
		return 1
	else:
		k = coins[i]
		total = 0
		if n % k == 0:
			total += 1
		while n > 0:
			total += ways(n, i-1)
			n -= k
	return total

print(ways(200, 7))
