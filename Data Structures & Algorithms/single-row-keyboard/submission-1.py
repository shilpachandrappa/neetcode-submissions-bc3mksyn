class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        charmap = {char: i for i, char in enumerate(keyboard)}
        count = 0
        prev_char = 0
        for char in word :
            count += abs(charmap[char] - prev_char)
            prev_char = charmap[char]
        return count