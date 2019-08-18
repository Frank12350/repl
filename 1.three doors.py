import random
# step1. 準備三道門]
doors = ["goot"] * 2
c = random.randint(0, 2)
doors.insert(c, "car")
print("一開始的門:", doors)
# step2. 參賽者選一道
c = random.randint(0, 2)
print("參賽者選:", doors[c])
del doors[c]
print("剩下的兩門:", doors)
# step3. 主持人在剩下的兩個中開一隻羊
doors.remove("goot")
print("剩下的一門:", doors)
# step4. 檢查參賽者帶回家的門是什麼
if doors[0] == "car":
  print("WIN")
else:
  print("LOSE")