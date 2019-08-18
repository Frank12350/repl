from random_words import RandomWords
import random
rw = RandomWords()
word = rw.random_word()

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
else:
  print("猜錯了")
  print("正確答案:", word)