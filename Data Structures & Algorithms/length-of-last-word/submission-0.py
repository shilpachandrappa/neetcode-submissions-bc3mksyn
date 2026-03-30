class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s.rstrip()
        word_len, index = 0, len(s)-1
        while index >= 0 and s[index] != ' ':
            word_len += 1
            index -= 1
        return word_len
            