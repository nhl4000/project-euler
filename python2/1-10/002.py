sum = 0;
fibonacci = 1;
x_0 = 0;
x_1 = 1;
while (fibonacci < 4000000):
	fibonacci = x_1 + x_0;
	x_0 = x_1;
	x_1 = fibonacci;
	if (fibonacci % 2 == 0):
		sum += fibonacci;
	
print(sum)
