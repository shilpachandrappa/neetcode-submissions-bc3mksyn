class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1 , index2 = 0,0
        result = []
        while index1 < len(word1) and index2 < len(word2) :
            result.append(word1[index1])
            result.append(word2[index2])
            index1 += 1
            index2 += 1
        if index1 < len(word1) :
            result.append(word1[index1:])
            
        if index2 < len(word2) :
            result.append(word2[ index2 :])
            
        return "".join(result)