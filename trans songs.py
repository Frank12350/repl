from googletrans import Translator
import os
import glob
for p in glob.glob("songs chinese/*.txt"):
  f = open(p)
  s = f.read()
  f.close()

  translator = Translator()
  result = translator.translate(s, dest='en')
  print(result.text)


  dname = "english"
  if not os.path.exists(dname):
    os.makedirs(dname)
  rp = p.replace("songs chinese", dname, 1)
  f = open(rp, "w")
  f.write(result.text)
  f.close()