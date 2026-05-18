class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words :
            l = 0
            for i in range(len(word)) :
                if word[i] not in allowed :
                    exit
                else :
                    l += 1
            if len(word) == l :
                count += 1
        return count