print(chr(97))
print(ord(A))
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = []
        for s in words:
            s_morse = ""
            for c in s:
                 s_morse = s_morse + morse[ord(c)-97]
            if s_morse not in result:
                result.append( s_morse )
        return len(result)                
                