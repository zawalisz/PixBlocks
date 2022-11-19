def fibonacci(number):
	a, b = 0, 1
	while (number-1 > 0):
		b += a
		a = b - a
		number -= 1
	return(b)

number = int(input("Write the number of fibonacci sequence: "))
print(fibonacci(number))