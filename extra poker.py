import random
import pokerdef
times = 0
while True:
  times = times + 1
  deck = []
  for c in range(4):
    for n in range(13):
      card=(c,n)
      deck.append(card)
  random.shuffle(deck)

  hands = []
  for i in range(5):
    c = deck.pop()
    print(pokerdef.trans(c))
    hands.append(c)
  print(hands)

  result = {}
  for c, n in hands:
    if n in result:
          result[n] = result[n] + 1
    else:
          result[n] = 1
  print(result)

  maximum = 0
  for k, v in result.items():
    if v > maximum:
          maximum = v
  print("最大重複:", maximum)

  if maximum == 4:
    print("鐵支!")
    print("總共", times, "次")
    break
