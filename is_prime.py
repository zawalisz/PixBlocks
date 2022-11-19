number = int(input("Write a number: "))

def is_prime(number):
	if(abs(number) <= 1):
		return False
	for i in range(2, number):
		if(number % i == 0):
			return False
	return True

print(is_prime(number))