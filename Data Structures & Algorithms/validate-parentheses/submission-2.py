class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            # closing cases:
            if c == ']' and stack and stack.pop() == '[':
                continue
            elif c == '}' and stack and stack.pop() == '{':
                continue
            elif c == ')' and stack and stack.pop() == '(':
                continue
            #opening cases
            elif c == '{' or c == '[' or c == '(':
                stack.append(c)
            # false case - i.e. a closed bracket without matching opening in stack
            else:
                return False
        
        if not stack:
            return True
        return False