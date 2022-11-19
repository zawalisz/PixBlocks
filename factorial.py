def factorial(number):
	if number < 2:
		return 1
	else:
		return number * factorial(number - 1)

number = int(input("write number: "))
print(factorial(number))