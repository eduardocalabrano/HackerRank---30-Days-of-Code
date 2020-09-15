class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        suma = 0;
        for c1 in range(1, n+1):
            if(self.encuentraDivisor(c1, n)):
                suma += c1
        return(suma)

    def encuentraDivisor(self, divisor, n):
        if(n % divisor == 0):
            return(True)
        else:
            return(False)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
