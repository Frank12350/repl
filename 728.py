class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for c in range(left, right+1):
            ccopy = c
            if not "0" in str(c):
                while True:
                    divisor = c % 10
                    if not ccopy % divisor == 0:
                        break
                    c = c // 10
                    if c == 0:
                        result.append(ccopy)
                        break
        return result