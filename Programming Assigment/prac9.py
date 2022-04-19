# Write Pythonic code to create a function named moverectangle() that takes  an object of Rectangle class and two numbers named dx and dy. It should  change the location of the Rectangle by adding dx to the x coordinate of
# corner and adding dy to the y coordinate of corner

#  Name: Aksh k Desai
# Id: 20CE020
# Github Repository Link: https://github.com/AKSHDESAI1/CE259_Python_Practicals.git

class Point(object):
    """Represent a Point Class"""


class Rectangle(object):
    """Represent a Rectangle Class"""


rectangle = Rectangle()

bottom_left = Point()
bottom_left.x = 3.0
bottom_left.y = 5.0

top_right = Point()
top_right.x = 5.0
top_right.y = 10.0

rectangle.corner1 = bottom_left
rectangle.corner2 = top_right

dx = 5.0
dy = 12.0


def move_rectangle(rectangle, dx, dy):
    print(f"The rectangle started with bottom left corner at ({rectangle.corner1.x},{rectangle.corner1.y})"
          f"\nTop right corner at ({rectangle.corner2.x},{rectangle.corner2.y})"
          f"\ndx is {dx} and dy is {dy}")
    rectangle.corner1.x = rectangle.corner1.x + dx
    rectangle.corner2.x = rectangle.corner2.x + dx
    rectangle.corner1.y = rectangle.corner1.y + dy
    rectangle.corner2.y = rectangle.corner2.y + dy
    print(f"It ended with a bottom left corner at ({rectangle.corner1.x},{rectangle.corner1.y})"
          f"\nTop right corner at ({rectangle.corner2.x},{rectangle.corner2.y})")


move_rectangle(rectangle, dx, dy)
