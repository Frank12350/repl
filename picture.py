from urllib.request import urlopen,urlretrieve
import json
import os
for m in range(12):
  url="https://www.google.com/doodles/json/2019/"+ str(m + 1) + "?hl=zh_TW"
  f=urlopen(url)
  images = json.load(f)
  for img in images:
    imgurl = "https:" + img["url"]
    print(img["title"])
    fn = imgurl.split("/")[-1]
    dn = "images"+ str(m + 1)
    if not os.path.exists(dn):
      os.makedirs(dn)
    full = dn + "/" + fn
    urlretrieve(imgurl, full)