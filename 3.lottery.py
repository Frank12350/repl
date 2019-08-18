import random
def buyticket():
  lottery = set()
  while len(lottery) < 7:
    n = random.randint(1, 49)
    lottery.add(n)
  return lottery

win = buyticket()
print("這期中獎號碼", win)

buy = 0
while True:
  my = buyticket()
  buy = buy + 1
  total = len(win & my)
  if total >= 7:
    print("恭喜")
    print("中獎數字", win & my)
    print("買了", buy, "張")
    break