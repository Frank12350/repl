rightusr = "frankie12350"
rightpwd = "guved958330"
inputusr = input("輸入妳的帳號")
inputpwd = input("輸入妳的密碼")
if not inputusr.lower() == rightusr.lower():
  print("妳是不是忘記帳號了!!!")
else:
  if inputpwd == rightpwd:
    print("成功登入")
  else:
    print("妳是不是忘記密碼了")
