def trans(c) :
    colortrans = ["\u2663", "\u2666", "\u2665", "\u2660"]
    numbertrans = ["2", "3", "4", "5", "6", "7",
               "8", "9", "10", "J", "Q", "K",
               "A"]
    return colortrans[c[0]] +" "+ numbertrans[c[1]]