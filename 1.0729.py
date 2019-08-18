def bmi(w, h):
    result = w / (h / 100) ** 2
    return round(result, 2)

print(bmi(75, 175))
print(bmi(80, 180))

result = 0
for times in range(10):
  result = result + (times + 1)
  print(result)

def addto(n):
  if n == 1:
    return 1
  else:
    print("addto", n - 1)
    return addto(n - 1) + n
print(addto(10))

def multiplyto(n):
  if n == 1:
    return 1
  else:
    print("multiply", n - 1)
    ans = multiplyto(n - 1) * n
    print("ans", ans)
    return ans
print(multiplyto(5))

def draw(layer):
  if layer == 1: 
    print("*")
  else:
    draw(layer - 1)
    print("*" * layer)
draw(20)