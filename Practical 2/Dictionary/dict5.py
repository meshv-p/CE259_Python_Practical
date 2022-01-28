'''
    Aim: Write a Python script to concatenate following dictionaries to create a new one. Sample Dictionary :
            dic1={1:10, 2:20}
            dic2={3:30, 4:40}
            dic3={5:50,6:60}
            Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    Name: Meshv U Patel
    Id: 20CE092
    Link: https://github.com/meshv-p/CE259_Practical-2_Assignment.git
'''

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict4 = {}
for i in (dic1, dic2, dic3):
    dict4.update(i)
print(dict4)