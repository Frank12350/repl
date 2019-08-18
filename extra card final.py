# ㄧ張撲克牌: (花色, 數字)
# 花色 0 - 3 數字 0 - 12
import random
import pokerdef
times = 0
while True:
    times = times + 1
    deck = []
    for c in range(4):
        for n in range(13):
            card = (c, n)
            deck.append(card)
    random.shuffle(deck)

    hands = []
    for i in range(5):
        c = deck.pop()
        print(pokerdef.trans(c))
        hands.append(c)
    print(hands)

    # Step1. 把次數字典做出來(重要)
    result = {}
    for c, n in hands:
        # 第二次以上遇到
        if n in result:
            result[n] = result[n] + 1
        # 第一次遇到
        else:
            result[n] = 1
    print(result)
    # Step2. 來找出最大次數
    maximum = 0
    for k, v in result.items():
        if v > maximum:
            maximum = v
    print("最大重複:", maximum)
    # Step3. 判斷
    if maximum == 4:
        print("鐵支!")
        print("總共", times, "次")
        break
