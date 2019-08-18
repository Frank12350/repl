import random
# 0: 梅花(最小) 3: 黑桃(最大)
# 0: A(最小) 12: K(最大)
com_color = random.randint(0, 3)
com_number = random.randint(0, 12)
print("電腦花色:", com_color)
print("電腦數字:", com_number)
player_color = random.randint(0, 3)
player_number = random.randint(0, 12)
print("玩家花色:", player_color)
print("玩家數字:", player_number)
if com_number>player_number:
  print("you lose")
elif com_number==player_number and com_color>player_color :
  print("you lose")
elif com_number==player_number and com_color==player_color :
  print("FLAT")
else:   
   print("VICTORY")
