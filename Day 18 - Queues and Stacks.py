import sys

class Solution:
    def __init__(self):
        self.cola = []
        self.pila = []
    def pushCharacter(self, element):
        self.pila.append(element)
    def enqueueCharacter(self, element):
        self.cola.reverse()
        self.cola.append(element)
        self.cola.reverse()
    def popCharacter(self):
        #el ultimo en entrar es el primero en salir
        largo = len(self.pila)
        caracter = self.pila[largo - 1]
        self.pila.pop(largo - 1)
        return(caracter)
    def dequeueCharacter(self):
        #el primero en entrar es el primero en salir
        largo = len(self.cola)
        caracter = self.cola[largo - 1]
        self.cola.pop(largo - 1)
        return(caracter)

# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
