class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = [0]*26
        for char in s:
            s_counter[ord(char)-ord('a')] += 1

        for char in t:
            index = ord(char)-ord('a')
            s_counter[index] -= 1
            if s_counter[index] < 0:
                return False
        return True