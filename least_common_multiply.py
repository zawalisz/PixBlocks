a = int(input("Write first number: "))
b = int(input("Write second number: "))

def least_common_multiply(a, b):
	for i in range(a, a * b + 1):
		if i % a==0 and i % b==0:
			return i

print(least_common_multiply(a, b))