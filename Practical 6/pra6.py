'''
    Name: Meshv U Patel
    Id: 20CE092
    Link: https://github.com/meshv-p/CE259_Python_Practical
    Aim: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 
'''
# find the number of occurences of each word
'''input: 4 
        bcdef 
        abcdefg 
        bcde 
        bcdef 
    output:3 
            2 1 1 
'''
a = int(input())
arr = []
for i in range(a):
    b = input()
    arr.append(b)
set1 = set(arr)
print(len(set1))

arr2 = []
arr3 = []
for i in arr:
    if i in arr2:
        pass
    else:
        arr2.append(i)
        arr3.append(arr.count(i))

for j in arr3:
    print(j, end=' ')




   





