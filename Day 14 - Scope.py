class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here

    def computeDifference(self):
        self.maximumDifference = 0
        for contador in range(len(self.__elements)):
            for c2 in range(len(self.__elements)):
                if(contador >= c2):
                    continue
                else:
                    absoluto = abs(self.__elements[contador] - self.__elements[c2])
                    if(absoluto > self.maximumDifference):
                        self.maximumDifference = absoluto
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
