class Solution:
    def validPalindrome(self, s: str) -> bool:
        left , right = 0, len(s)-1
        def isPalindrome(s,left,right):
            while left < right :
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        while left < right :
            if s[left] == s[right] :
                left += 1
                right -= 1
            else :
                return isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1)
        return   True