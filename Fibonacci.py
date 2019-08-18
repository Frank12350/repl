result = 0
times = 0
while times < 10:
  result = result + (times + 1)
  times = times + 1
print(result)

# 前前一項
result1 = 0
# 前一項
result2 = 0
times = 0
while times < 13:
  if times == 0:
    result1 = 0
    print(0)
  elif times == 1:
    result2 = 1
    print(1)
  else:
    new = result1 + result2
    print(new)
    result1 = result2
    result2 = new
  times = times + 1