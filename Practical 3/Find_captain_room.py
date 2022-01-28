'''
    Name: Meshv U Patel
    Id: 20CE092
    Link: https://github.com/meshv-p/CE259_Practical-2_Assignment.git
'''
leng = int(input())
numbers = [int(i) for i in input().split()]
for i in numbers:
    if numbers.count(i) == 1:
        print(i)