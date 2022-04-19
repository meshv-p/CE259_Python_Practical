# Explain about the different types of Exceptions in Python with suitable example./
# Name: Meshv Patel
# Id: 20CE092
# Github Repository Link: https://github.com/meshv-p/CE259_Python_Practical

try:
    a = 10/0
    print(a)
except ArithmeticError:
    print("This statement is raising an arithmetic exception.")
else:
    print("Success.")

try:
    a = [1, 2, 3]
    print(a[3])
except LookupError:
    print("Index out of bound error.")

import math

print(math.exp(1000))

array = [0, 1, 2]
print(array[3])
