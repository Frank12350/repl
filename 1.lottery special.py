import random
def buyticket():
  lottery = set()
  while len(lottery) < 6:
    n = random.randint(1, 49)
    lottery.add(n)
  return lottery

win = buyticket()
print("這期中獎號碼", win)
while True:
  special = random.randint(1, 49)
  if not special in win:
    break
print("特別號", special)

