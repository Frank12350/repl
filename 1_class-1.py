class Person:
  name = None
  height = None
  weight = None

p1 = Person()
p1.name = "Joe"
p1.weight = 60
p1.height = 170
bmi = p1.weight / (p1.height / 100) ** 2
print(bmi)