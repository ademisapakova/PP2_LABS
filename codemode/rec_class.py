from re import X
from tkinter import Y


class Rectangle:
    def __init__(self, w, h, c):
        self.width = w
        self.height = h
        self.color = c


    def get_area(self):
        return self.width*self.height 

    def get_perimeter(self):
        return 2*self.width+2*self.height       

    def change_color(self, color):
        self.color = color   

    def compare_areas(self, R):
        if self.get_area() > R.get_area():
            return self.get_area() 
        else:
            return R.get_area()    




def compare_area2(R1, R2):
    return R1.get_area() > R2.get_area()


R1= Rectangle(30,40,'blue')   
R2= Rectangle(500,10,'black')        

print(R1.get_area())
R1.change_color('red')

print(R1.color)

is_bigger = compare_area2(R1,R2)
is_bigger2=R1.compare_areas(R2)

print(is_bigger2)