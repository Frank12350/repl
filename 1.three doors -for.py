import random
win = 0
lose = 0
for times in range(500000):
  # step1. 準備三道門]
  doors = ["羊"] * 2
  c = random.randint(0, 2)
  doors.insert(c, "車")
  #print("一開始的門:", doors)
  # step2. 參賽者選一道
  c = random.randint(0, 2)
  #print("參賽者選:", doors[c])
  del doors[c]
  #print("剩下的兩門:", doors)
  # step3. 主持人在剩下的兩個中開一隻羊
  doors.remove("羊")
  #print("剩下的一門:", doors)
  # step4. 檢查參賽者帶回家的門是什麼
  if doors[0] == "車":
    win = win + 1
  else:
    lose = lose + 1
print("贏次數:", win)
print("輸次數:", lose)
total = win + lose
print("贏機率:", win/total*100, "%")
print("輸機率:", lose/total*100, "%")