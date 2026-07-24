from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord(char)-ord('a')] += 1
            freq_str = tuple(freq)
            anagrams[freq_str].append(word)
        return list(anagrams.values())