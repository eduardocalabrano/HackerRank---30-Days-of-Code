class Person:
    def __init__(self,initialAge):
        if(initialAge > 0):
            self.age = initialAge
        else:
            self.age = 0
            print('Age is not valid, setting age to 0.')
    def amIOld(self):
        if(self.age < 13):
            print('You are young.')
        elif(self.age >= 13 and self.age < 18):
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        self.age = self.age + 1

t = int(input())
if(t >= 1 and t <= 4):
    for i in range(0, t):
        age = int(input())
        if(age >= -5 and age <= 30):
            p = Person(age)
            p.amIOld()
            for j in range(0, 3):
                p.yearPasses()
            p.amIOld()
            print("")
