from jieba import cut, set_dictionary, load_userdict
from jieba.analyse import extract_tags 
from urllib.request import urlretrieve
import glob

url = "https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big"
urlretrieve(url, "dict.txt.big")
set_dictionary("dict.txt.big")
load_userdict("entertainment.txt")

for p in glob.glob("1.news/*.txt"):
  f = open(p)
  s = f.read()
  f.close()

  print(p, extract_tags(s, 10))