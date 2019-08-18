from urllib.request import urlopen
from bs4 import BeautifulSoup
f = open("tabelog.txt", "w")

page = 51
while True:
  print("頁數", page)
  url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
  try:
    response = urlopen(url)
  except:
    f.close()
    print("結束")
    break   
  html = BeautifulSoup(response)
  rs = html.find_all("li", class_="list-rst")
  for r in rs:
    en = r.find("a", class_="list-rst__name-main")
    ja = r.find("small", class_="list-rst__name-ja")
    rating = r.find("b", class_="c-rating__val")
    print(rating.text, ja.text, en.text)
    c = rating.text + "\t" + ja.text + "\t" + en.text + "\n"
    f.write(c)
  page = page + 1
