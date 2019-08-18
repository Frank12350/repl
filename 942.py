class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        top = len(S)
        bottom = 0
        result = []
        for c in S:
            if c=="I":
                result.append(bottom)
                bottom = bottom + 1
            else:
                result.append(top)
                top = top -1
        result.append(top)
        return result