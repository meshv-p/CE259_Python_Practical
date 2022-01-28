'''
    Aim:  Write a Python program to sum all the items in a dictionary.
    Name: Meshv U Patel
    Id: 20CE092
    Link: https://github.com/meshv-p/CE259_Practical-2_Assignment.git
'''

numbers = {'a':1,'b':10,"c":2}

def sumAllItems(dic):
    sum =0  
    for key , value in dic.items():
        sum = sum + value
    return sum

finalsume = sumAllItems(numbers)
print(finalsume)