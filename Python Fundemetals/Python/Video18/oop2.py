import math

class Point:
    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y

    def __str__(self):
        return "<{},{}>".format(self.x_cord, self.y_cord)

    def euclidean_distance(self, other):
        return math.sqrt(
            (other.x_cord - self.x_cord) ** 2 +
            (other.y_cord - self.y_cord) ** 2
        )

    def point_on_line(self, m, c):
        # y = mx + c
        return self.y_cord == (m * self.x_cord + c)


p1 = Point(2, 5)
p2 = Point(6, 8)

print(p1)
print(p2)

print("Distance =", p1.euclidean_distance(p2))

# Check if point lies on line
print(p1.point_on_line(2, 1))



# How objects  access
class Person:
    def __init__(self, name_input, country_input):
        self.name = name_input
        self.country = country_input

    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}"


p1 = Person("Rahul", "Bangladesh")

p1.name = "Raftes"

print(p1.name)
print(p1)

# Reference variables

class Person:
    def __init__(self):
        self.name="Rahul"
        self.gender="Male"

p=Person()
q=p


class Person1:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# Outside the class -> normal function
def greet(pe):
    print("Hello", pe.name)


p1 = Person1("Rahul", "Male")

greet(p1)
