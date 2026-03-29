class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '*', '/', '-'}
        for t in tokens:
            if t in ops:
                a = int(stack.pop())
                b = int(stack.pop())
                if t == '+':
                    res = str(a+b)
                elif t == '-':
                    res = str(b-a)
                elif t == '/':
                    res = str(int( float(b) / a))
                else:
                    res = str(a*b)
            else:
                res = t
            stack.append(res)
        return int(stack.pop())
            