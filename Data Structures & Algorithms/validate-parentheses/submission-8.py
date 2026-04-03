class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{', ')':'(', ']':'['}
        for char in s :
            if char in '({[':
                stack.append(char)
            elif stack and char in mapping and stack[-1] == mapping[char] :
                top = stack.pop()
            else :
                return False
        return len(stack)==0
