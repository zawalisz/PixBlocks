a = int(input("Write first number: "))
b = int(input("Write second number: "))

def greatest_common_divisor(a, b):
	for i in range(1, a + 1):
		if a % i == 0 and b % i == 0:
			max = i
	return(max)

print(greatest_common_divisor(a, b))