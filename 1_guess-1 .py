import random
low = 1
high = 100
ans = random.randint(low, high)
while True:
    msg = "請輸入" + str(low) + "~" + str(high)
    g = int(input(msg))
    if g > ans:
        high = g
    elif g < ans:
        low = g
    else:
        print("猜對了")
        break