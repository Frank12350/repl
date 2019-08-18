class Person:
    name = None
    height = None
    weight = None
    def setvalue(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def bmi(self):
        b = self.weight / (self.height / 100) ** 2
        return b

p1 = Person()
p1.setvalue("Joe", 170, 60)
print(p1.bmi())