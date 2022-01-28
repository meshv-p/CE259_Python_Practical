'''
    Aim:  Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
    Name: Meshv U Patel
    Id: 20CE092
    Link: https://github.com/meshv-p/CE259_Practical-2_Assignment.git
'''

def most_CommonList(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num, counter


List = [2, 1, 1, 1, 2, 1, 3]
common = most_CommonList(List)
print(f'Your most common Elements in list is {common[0]} and this is repeat {common[1]} times.')

# element in a tuple
def commonElement_tuple(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num, counter


List = (3, 4, 5, 4, 3, 2, 1, 2, 3)
common1 = commonElement_tuple(List)
print(f'Your most common Elements in tuple is {common1[0]} and this is repeat {common1[1]} times.')


# most common elements in dictionary
a = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 2}
lis = []
for i in a.values():
    lis.append(i)


def most_CommonDictionary(List):
    counter = 0
    num = List[0]

    for j in List:
        curr_frequency = List.count(j)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = j

    return num, counter


common2 = most_CommonDictionary(lis)
print(f'Your most common Elements in Dicionary is {common2[0]} and this is repeat {common2[1]} times.')