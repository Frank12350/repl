from game import Machine

m = Machine(h=200)
while True:
    g = int(input(m.show()))
    if m.guess(g) == True:
        print("猜對了")
        break