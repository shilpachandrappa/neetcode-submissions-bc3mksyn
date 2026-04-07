class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        charmap = {char: i for i, char in enumerate(keyboard)}
        count = 0
        prev_char = 0
        for char in word :
            target_char = charmap[char]
            count += abs(target_char - prev_char)
            prev_char = target_char
        return count