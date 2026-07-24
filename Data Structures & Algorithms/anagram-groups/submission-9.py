from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            word_freq = [0]*26
            for char in word:
                word_freq[ord(char)-ord('a')] += 1
            word_freq_str = tuple(word_freq)
            anagrams[word_freq_str].append(word)
        return list(anagrams.values())