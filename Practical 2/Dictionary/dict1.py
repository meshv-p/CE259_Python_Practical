'''
    Aim: Write a Python script to check whether a given key already exists in a dictionary.
    Name: Meshv U Patel
    Id: 20CE092
    Link: https://github.com/meshv-p/CE259_Practical-2_Assignment.git
'''

sample = {
    "name":"Meshv",
    "subject":"PIP",
    "language":"Python"
}
def checkKey(key):
    if sample[key]:
        print(f'{key} Key is present in the dictionary')
    else:
        print(f'{key} Key is not present in the dictionary')

checkKey("name")
