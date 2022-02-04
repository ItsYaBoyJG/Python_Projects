"""
accept coordinates as a pair of tuples and return the slope and distance of the line

find volume and surface area of a cylinder

"""
import math


# distance and slope formula using variables as tuples
class Line:

    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    # using the distance formula
    def distance(self):
        x, a = self.cord1  # x = x1  a = y1
        y, b = self.cord2  # y = x2 b = y2
        return math.sqrt(((x - y) ** 2) + ((a - b) ** 2))  # distance formula

    # using formula for slope
    def slope(self):
        x, a = self.cord1  # same as above x1,y1
        y, b = self.cord2  # x2,y2
        return (b - a) / (y - x)  # slope formula


# user input
print("Enter the first coordinate ")
x1, y1 = map(int, input().split())
print("Enter the second coordinate ")
x2, y2 = map(int, input().split())

line1 = (x1, y1)
line2 = (x2, y2)

#  Line() is needed to be able to input variables in class
li = Line(line1, line2)

print("The distance is ", li.distance())

print("The slope is ", li.slope())


class Cylinder:

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    # finds volume using standard formula
    def volume(self):
        h = self.height
        r = self.radius
        return h * 3.14159 * (r ** 2)

    # finds SA using standard formula
    def surface_area(self):
        s_area = self.radius
        h = self.height
        r = self.radius
        return (2 * s_area) + 2 * 3.14 * h * r


print("Enter the height or the cylinder")
user_h = float(input())
print("Enter the radius ")
user_r = float(input())

user_vol = Cylinder(user_h, user_r)

print("The volume is ", user_vol.volume())
print("The surface area is ", user_vol.surface_area())
