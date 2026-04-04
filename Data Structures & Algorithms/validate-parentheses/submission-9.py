class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        mapping = {')':'(',
                ']':'[',
                '}' : '{'}
        for char in s :
            if char in '({[':
                stack.append(char)
            else :
                if stack and mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
                           