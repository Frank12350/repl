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

buy = 0
while True:
  my = buyticket()
  buy = buy + 1
  score = len(my & win) * 2
  if special in my:
    score = score + 1
  if score >= 11:
    print("恭喜, 二獎以上")
    print("中獎彩券", my)
    print("分數", score)
    print("總共買", buy, "張")
    break  
