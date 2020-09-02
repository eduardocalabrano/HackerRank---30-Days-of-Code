class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        Person.__init__(self, firstName, lastName, idNum)
        self.notas = scores

    def calculate(self):
        promedio = self.__calcula_promedio()
        letter = ''
        if(promedio <= 100 and promedio >= 90):
            letter = 'O'
        elif(promedio < 90 and promedio >= 80):
            letter = 'E'
        elif(promedio < 80 and promedio >= 70):
            letter = 'A'
        elif(promedio < 70 and promedio >= 55):
            letter = 'P'
        elif(promedio < 55 and promedio >= 40):
            letter = 'D'
        elif(promedio < 40):
            letter = 'T'
        return(letter)

    def __calcula_promedio(self):
        acumulado = 0
        for nota in self.notas:
            acumulado += nota
        else:
            return(acumulado/len(self.notas))

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
#numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
