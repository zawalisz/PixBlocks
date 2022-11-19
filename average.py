print('This program counts an averege value for given numbers')
print('and gives this one from given numbers,')
print('that is the nearest average value.')
numbers = []
number = int(input('Write a number: '))

while number != 's':
   numbers.append(int(number))
   number = input('Write a number or "s" if you do not want to write more numbers: ')

sum = 0

for j in numbers:
	sum += int(j)
	
avg = float(sum) / len(numbers)

index = 0

for j in numbers:
	if abs(int(j) - avg) < abs(int(numbers[index]) - avg):
		index = numbers.index(j)
		
print(numbers[index])