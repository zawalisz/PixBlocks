def power(base, exponent):
	if exponent == 0:
		return 1
	else:
		return base * power(base, exponent - 1)
		
base = int(input("Write the base of power: "))
exponent = int(input("Write the exponent: "))
print(power(base, exponent))