"program to perfrom basic operation of maths using math module"

import math as mt
num = int (input("Enter a number"))
squareroot = mt.sqrt(num)
log = mt.log(num)
sine = mt.sin(num)
print(f"The square root of{num} is {squareroot}.")
print(f"The natural log of {num} is {log}.")
print(f"The sine of {num} in radian is {sine}.")