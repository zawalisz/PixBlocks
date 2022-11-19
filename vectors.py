print("The program sorts the vectors by length ascending.")
print("First point of each vector is in [0,0].")

import math

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.distance = math.sqrt(self.x ** 2 + self.y ** 2)
	
	def __str__(self):
		return "[{0}, {1}]".format(self.x, self.y)
	
	def __lt__(self, other):
		return self.distance < other.distance	
	
vectors = []
point = ''
while point != 'c':
    point = input('Write coordinates of second point saparated by a coma ("X,Y") or "c" to complit input: ')
    if point != 'c':
        x, y = float(point.split(',')[0]), float(point.split(',')[1])
        vector = Vector(x, y)
        vectors.append(vector)
	
vectors.sort()
	
for i in vectors:
	print(i)