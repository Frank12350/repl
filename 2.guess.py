# https://reurl.cc/r78gE
from random_words import RandomWords
import random
i = 0
score = 0
while i < 10:
  # 原本的文字
  rw = RandomWords()
  word = rw.random_word()
  # 替換一個字母的文字
  c = random.randint(0, len(word) - 1)
  times = 0
  news = ""
  while times < len(word):
    if times == c:
      news = news + "_"
    else:
      news = news + word[times]
    times = times + 1
  print("謎題:", news)
  # 使用者猜一下
  guess = input("猜:")
  if guess == word:
    print("猜對了")
    score = score + 1
  else:
    print("猜錯了")
    print("正確答案:", word)
  i = i + 1
print("總分:", score * 10)