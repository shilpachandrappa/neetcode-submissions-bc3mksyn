class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_count = Counter(s)
        one_char = False
        for each_count in char_count.values() :
            if each_count % 2 != 0 :
                if one_char :
                    return False
                one_char = True

        return True