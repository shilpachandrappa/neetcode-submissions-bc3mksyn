class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) <= 1 :
            return 0
        pointer = 1
        total = 0
        while pointer <  len(s) :
            total += abs(ord(s[pointer]) - ord(s[pointer-1]))
            pointer+= 1
        return total