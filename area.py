c=int(input("[0]正方形 [1]長方形 [2]圓形 [3] 三角形"))

if c==0:
  w=float(input("請輸入邊長"))
  print("正方形面積:", w**2)
elif c==1:
  l=float(input("請輸入長"))
  w=float(input("請輸入寬"))
  print("長方形面積:",l*w)
elif c==2:
  r=float(input("請輸入半徑:"))
  pi=3.14159265359
  print("圓形面積: ",pi*(r**2))
elif c==3:
  w4=float(input("請輸入底"))
  w5=float(input("請輸入高:"))
  print("三角形面積: ",w4*w5/2)
else :
  print("error")
