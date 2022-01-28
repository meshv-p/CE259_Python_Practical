'''
    Aim: Write a Python program to remove an item from a set if it is present in the set.
    Name: Meshv U Patel
    Id: 20CE092
    Link: https://github.com/meshv-p/CE259_Practical-2_Assignment.git
'''

def removeElement(element):
    if element in a:
        a.discard(element)
        return a
    else:
        return 'This element does not exist in set'


a = set([1, 2, 3, 4])
print(removeElement(2))