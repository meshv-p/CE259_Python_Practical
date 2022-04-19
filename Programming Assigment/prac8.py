# Program to demonstrate the Overriding of the Base Class method in the Derived Class.

# Name: Aksh k Desai
# Id: 20CE020
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Python_Practicals.git

class P1_class():

    def show(self):
        print("Inside Parent Class 1")


class P2_class():

    def display(self):
        print("Inside Parent Class 2")


class Child_class(P1_class, P2_class):

    def show(self):
        print("Inside Child Class")


obj = Child_class()

obj.show()
obj.display()
