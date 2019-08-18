print("十進位->二進位")
c = int(input("輸入整數"))

s = ""
while True:
  # 取商
  div = c // 2
  # 取餘數
  add = c % 2
  # 先記錄餘數
  s = s + str(add)
  # 如果商=0, 該結束 
  if div == 0:
    break
  # 否則把c設定div, 繼續除下去
  else:
    c = div
print(s[::-1])