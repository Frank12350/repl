import random
player = int(input("請出拳[0]棒[1]老虎[2]雞[3]蟲"))
com =random.randint(0, 3)
print("you:",player)
print("computer:",com)

if com==(player+1)%4:
  print("VICTORY")
elif player==(com+1)%4 :
  print("you lose")
else:
  print("FLAT")    