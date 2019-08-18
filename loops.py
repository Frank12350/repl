times = 0
while times < 10:
  print(times + 1, "hello")
  times = times + 1

times = 0
while times < 10:
  print(4* times + 1, "hello")
  times = times + 1

times = 0
while times < 10:
  print("*" * (times + 1))
  times = times + 1
times = 0
while times < 10:
  i = times + 1
  s = " " * (10 - i)  + "*" * i
  print(s)
  times = times + 1

times = 0
while times < 10:
  blank = " " * (10 - times - 1) 
  star = "*" * (2 * times + 1)
  s = blank + star
  print(s)
  times = times + 1