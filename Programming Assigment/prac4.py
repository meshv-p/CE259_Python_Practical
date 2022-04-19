# Given a list of integers, write a program to print the count of all possible unique combinations of numbers whose sum is equal to K. Input The first line of input will contain space-separated integers. The second  line of
# input will  contain an integer, denoting K. Output The output should be
# containing the count of  all  unique combinations of numbers whose  sum
# is equal to  K.


# Name: Meshv Patel
# Id: 20CE092
# Github Repository Link: https://github.com/meshv-p/CE259_Python_Practical

from itertools import combinations

num = [int(n) for n in input("Enter an array: ").split()]
k = int(input("Enter the sumation you want to check combination about: "))
cnt = 0
for i in range(1, len(num)+1):
    for c in combinations(num, i):
        if sum(c) == k:
            cnt += 1
print(cnt)
