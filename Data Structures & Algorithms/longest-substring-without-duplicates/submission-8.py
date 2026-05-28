class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_count = 0
        left =0
        for right in range(len(s)):
            while s[right] in seen :
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            
            #print(seen)
            #print(f"max_count - {right - left+1}")
            max_count = max(max_count, len(seen))
        return max_count

