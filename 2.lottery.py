import random
def buyticket():
  lottery = set()
  while len(lottery) < 7:
    n = random.randint(1, 49)
    lottery.add(n)
  return lottery

my = buyticket()
print(my)
win = buyticket()
print(win)

