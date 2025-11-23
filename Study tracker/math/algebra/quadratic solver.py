# Solves quadratic equations using the quadratic formula

import math

print("Quadratic Equation Solver")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Two real roots:", x1, x2)

elif discriminant == 0:
    x = -b / (2*a)
    print("One real root:", x)

else:
    print("No real roots (complex solutions).")
