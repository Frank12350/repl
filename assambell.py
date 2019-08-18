set1 = {5,6,8,9,}
set2 = {4,5,6,7}

# 交集: 我們都有的!!
print(set1 & set2)
# 聯集: 把所有都列出來
print(set1 | set2)
# 差集: 前面減後面
print(set2 - set1)

result = 0
for s in set1:
  print("+", s)
  result = result + s
  print("ans", result)
  
set1.add(6)
print(set1)
set1.add(5)
print(set1)

set1.discard(5)
print(set1)
set1.discard(15)
print(set1)