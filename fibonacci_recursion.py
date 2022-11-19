def fibonacci(number):
	if (number < 3):
		return 1
	else:
		return fibonacci(number-1)+fibonacci(number-2)

number = int(input("Write the number of fibonacci sequence: "))
print(fibonacci(number))