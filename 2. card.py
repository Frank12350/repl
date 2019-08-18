import random
# 0: 梅花(最小) 3: 黑桃(最大)
# 0: A(最小) 12: K(最大)
com_color = random.randint(0, 3)
com_number = 0
print("電腦花色:", com_color)
print("電腦數字:", com_number)
player_color = random.randint(0, 3)
player_number = random.randint(0, 12)
print("玩家花色:", player_color)
print("玩家數字:", player_number)

# 如果你要讓A最大
player_number = (player_number - 1) % 13
com_number = (com_number - 1) % 13
# 比大 vs 比小
c = int(input("[0]比大 [1]比小"))
if c == 1:
  player_color = 3 - player_color
  player_number = 12 - player_number
  com_color = 3 - com_color
  com_number = 12 - com_number

if player_number > com_number:
  print("我贏了")
elif player_number == com_number:
  if player_color > com_color:
    print("我贏了")
  elif player_color == com_color:
    print("平手")
  else:
    print("我輸了")
else:
  print("我輸了")
