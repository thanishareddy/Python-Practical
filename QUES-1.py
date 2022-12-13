"""
WAP to find the roots of a quadratic equation a quadratic equation is in the form:
ax**2 + bx + c = 0
"""

import cmath

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

# calculate the determinant
det = (b ** 2) - (4 * a * c)

# calculate solutions
sol1 = ((-b) - cmath.sqrt(det)) / (2 * a)
sol2 = ((-b) + cmath.sqrt(det)) / (2 * a)

print("The solutions of the quadratic equation are {0} and {1}".format(sol1, sol2))
