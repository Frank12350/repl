from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://tabelog.com/tw/tokyo/rstLst/?SrtT=rt"
response = urlopen(url)
html = BeautifulSoup(response)
rs = html.find_all("li", class_="list-rst")
for r in rs:
  en = r.find("a", class_="list-rst__name-main")
  print(en)