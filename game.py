import random
class Machine:
    def __init__(self, l=1, h=100):
        self.low = l
        self.high = h
        self.ans = random.randint(l, h)
    def guess(self, n):
        if n > self.ans:
            self.high = n
            return False
        elif n < self.ans:
            self.low = n
            return False
        else:
            return True
    def show(self):
        msg = "請輸入" + str(self.low) + "~" + str(self.high)
        return msg