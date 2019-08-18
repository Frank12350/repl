import random
player = int(input("請出拳[0]剪刀[1]石頭[2]布"))
com =random.randint(0, 2)
print("you:",player)
print("computer:",com)

if player==com:
  print("FLAT")
elif player==(com+1)%3 :
  print("VICTORY")
else:
  print("YOU LOSE")    