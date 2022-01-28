'''
    Aim:  Write a Python script to merge two Python dictionaries.
    Name: Meshv U Patel
    Id: 20CE092
    Link: https://github.com/meshv-p/CE259_Practical-2_Assignment.git
'''


sample = {
    "name":"Meshv",
    "subject":"PIP",
    "language":"Python"
}
sample2 = {
    "role":"Full-stack Webdeveloper",
    "languages":["React js","Python", "Django", "Django Rest Framework"]
}

def mergerDictionary(dict1,dict2):
    return dict1.update(dict2)

mergerDictionary(sample,sample2)
print(sample)
