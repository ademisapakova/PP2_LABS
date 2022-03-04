class Person:
    def __init__(self, age, sex):
        self.age = age 
        self.sex = sex



class Aibergen(Person):
    def __init__(self, age, sex, love):
        super().__init__(age, sex)
        self.love = love
    
    def luv(self):
        return ('{}: {}'.format('Amount of love he giving to Adema ', self.love))

class Adema(Person):
    def __init__(self, age, sex, support):
        super().__init__(age, sex)
        self.support = support

    def loving(self):
        return ('{}: {}'.format('Amount of support she giving to Aibergen ', self.support))


Adem = Adema(18,'F', 100)
Aibok = Aibergen(17, 'M', 101)

print(Adem.loving())
print(Aibok.luv())
print(Adem.sex)

