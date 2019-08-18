# 小數: 誤差(十進位的小數二進位表示有可能無法有有限位數表示)
print(3 + 3.14)
# (先給妳) 十進位小數, 不會有誤差
import decimal
print(decimal.Decimal("3") + decimal.Decimal("3.14"))

# 文字
s = "hello python"
print(s[4])
print(len(s))
# 拿到最後一個字
print(s[len(s) - 1])
# 第二個方法(Python)
print(s[-1])
# 某位置~某位置 [位置1:位置2 + 1]
print(s[4:9])
print(s[::2])
# 常用
print(s[::-1])

# 加法
s = s + " 3"
print(s)

# 換行(兩個字來組合一個字)
a = "hello\npython"
# \n: 長度1
print(len(a))
print(a)