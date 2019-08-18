def bmi(w, h):
    result = w / (h / 100) ** 2
    return round(result, 2)

print(bmi(75, 175))
print(bmi(94, 1170))

result = 0
for times in range(10):
  result = result + (times + 1)
  print(result)

def addto(n):
  if n == 1:
    return 1
  else:
    print("addto", n - 1)
    ans= addto(n - 1) + n
    print("ans"ans)
print(addto(11))