class Person:
    def __init__(self, gender, number_of_legs):
        self.gender =  gender
        self.number_of_legs = number_of_legs

class Student(Person):
    def __init__(self, loan, gender, number_of_legs):
        super().__init__(gender, number_of_legs)
        self.loan = loan 


P1 = Person('F', 2)
Ernat = Student(2500, 'M', 2)

print(Ernat.loan, Ernat.gender)



class Employee(Person):
    pass 

class Teacher(Employee):
    pass
