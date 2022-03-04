
from math import pi
class Figures:
    def __init__(self, color):
        self.color = color


class Circle(Figures):
    def __init__(self, radius, arc, color):
        self.radius = radius
        self.arc = arc
        super().__init__(color)

    def area(self):
        return pi*self.radius*self.radius 

    def c(self):
        return 2*pi*self.radius 



class Square(Figures):
    def __init__(self, a, color):
        self.a = a
        super().__init__(color)

    def area(self):
        return self.a*self.a

    def perimeter(self):
        return 4*self.a




def compare_areas(Cir, Sq):
    if Cir.area() > Sq.area():
        return Cir.area()
    else:
        return Sq.area()
Cir = Circle(4, 5, 'darkblue')
Sq = Square(20, 'pink')

print("Area of circle is", Cir.area())
print("Circumference if", Cir.c())
print("Area of square is", Cir.area())
print("Permeter is", Sq.perimeter())
print(compare_areas(Cir, Sq))




