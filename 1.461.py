class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        wrong = 0
        while True:
            if not x%2== y%2:
                wrong = wrong +1
            x = x//2
            y = y//2
            if x == 0 and y == 0:
                break
        return wrong
        