a = float( input("Enter your height : "))
b = float( input("Enter your weight : "))
BMI= b /( (a / 100) ** 2)
print("your weight is", a)
print("your hight is", b)
print("BMI is", BMI)

#判斷過重 正常 過輕
if BMI > 25:
  print("over weight")
  print("you need do more exercise.")
elif 18< BMI <= 25:
    print("normal")
else:
    print("over light")
    print("you need to eat more.")




