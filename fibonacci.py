number = int(input("Write the number of fibonacci sequence: "))

a, b = 0, 1

while (number > 0):
	print(b)
	b += a
	a = b - a
	
	number -= 1