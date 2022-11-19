print('Whether sections of given lengths can be formed into a triangle?')

a = int(input('Write the length of the first section: '))
b = int(input('Write the length of the second section: '))
c = int(input('Write the length of the third section: '))

print((a + b > c) and (a + c > b) and (b + c > a))