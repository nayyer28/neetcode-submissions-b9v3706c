class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
                if t == '+':
                    stack.append(stack.pop() + stack.pop())
                elif t == '-':
                    second,first = stack.pop(), stack.pop()
                    stack.append(first - second)
                elif t == '*':
                    stack.append(stack.pop() * stack.pop())
                elif t == '/':
                    second,first = stack.pop(), stack.pop()
                    stack.append(int( float(first) / second))
                else:
                    stack.append(int(t))
        return stack.pop()