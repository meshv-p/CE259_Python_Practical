# Write a procedure to find min, max, mean, standard deviation, variance  of  number list. Example Input :  10  50  80  70  49  23  11   4output :  4  80  37. 13  27. 25  848. 70

# Name: Meshv Patel
# Id: 20CE092
# Github Repository Link: https://github.com/meshv-p/CE259_Python_Practical

from cmath import sqrt
from statistics import median, variance

numbers = [10, 50, 80, 70, 49, 23, 11, 4]

print(min(numbers))
print(max(numbers))

print(median(numbers))

Variance = variance(numbers)

print(sqrt(Variance))

print(Variance)
