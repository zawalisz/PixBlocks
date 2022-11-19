number = int(input("Write a number: "))

import math
def is_square(number):
	if math.sqrt(number) % 1 == 0:
		return True
	else:
		return False

print(is_square(number))