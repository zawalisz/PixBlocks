V0 = int(input("Write the starting amount: "))
r = int(input("Write nominal annual interest rate: "))
n = int(input("Write the number of years: "))

V = round((V0 * (1 + r/100) ** n), 2)
print(V)