# Aim: You are  given a string. Your task  is to count the  frequency  of  letters  of  the  string  and print the letters in  descending  or der of frequency. If the  following  string is given  as input to the program: a a b b b c c d e Then, the output of the  program  should  be:
# b 3
# a  2
# c  2
# d  1
# e  1


# Name: Meshv U Patel
# Id: 20CE092
# Github Repository Link: https://github.com/meshv-p/CE259_Python_Practical
a = input()
dic = {}
for i in a:
    if dic.get(i) != None:
        dic[i] += 1
    else:
        dic[i] = 1
arr = [dic[i] for i in dic]
arr.sort(reverse=True)

dic1 = {}
for i in arr:
    for j in dic:
        if dic[j] == i:
            dic1.update({j: i})
            dic.pop(j)
            break

for key, value in dic1.items():
    print(key, value)
