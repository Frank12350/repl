class Person:

    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def bmi(self):
        b = self.weight / (self.height / 100) ** 2
        return b

p1 = Person("Elwing", 175, 75)
print(p1.bmi())
p2 = Person("Bob", 180, 80)
print(p2.bmi())