class Solution:
    def isValid(self, s: str) -> bool:
        #TC - O(N)
        #SC - O(N)
        # Stack to store opening brackets
        stack = []
        
        # Map each closing bracket to its matching opening bracket
        brackets = {')': '(', '}': '{', ']': '['}

        # Iterate over every character in the string
        for char in s:

            # If it's an opening bracket → push to stack
            if char in "({[":
                stack.append(char)

            # If it's a closing bracket and stack top matches → pop
            elif stack and char in brackets and stack[-1] == brackets[char]:
                stack.pop()

            # Otherwise → mismatch or closing bracket with empty stack → invalid
            else:
                return False

        # Valid only if no unmatched opening brackets remain
        return len(stack) == 0