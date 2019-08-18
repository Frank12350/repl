import random
lottery = set()
while len(lottery) < 7:
  print("!")
  n = random.randint(1, 49)
  lottery.add(n)
print(lottery)