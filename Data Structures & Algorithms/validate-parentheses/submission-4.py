class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = {'(', '{', '['}

        for c in s:
            if c == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif c == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif c == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif c in opens:
                stack.append(c)
            else:
                return False
        return len(stack) == 0
            