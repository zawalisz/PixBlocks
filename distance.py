import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def distance(self, other):
		return round(math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2), 2)

x1 = float(input("Write the X value of the first point: "))
y1 = float(input("Write the Y value of the first point: "))
x2 = float(input("Write the X value of the second point: "))
y2 = float(input("Write the Y value of the second point: "))

point1 = Point(x1, y1)
point2 = Point(x2, y2)

print(point1.distance(point2))