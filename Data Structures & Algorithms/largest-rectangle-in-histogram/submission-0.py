class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        mx_a = float("-inf")
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                pop_h, pop_i = stack.pop()
                base = i - pop_i
                mx_a = max(mx_a, base * pop_h)
                start = pop_i
            stack.append((h, start))
            print(stack, mx_a)
        
        while stack:
            print(stack)
            pop_h, pop_i = stack.pop()
            base = len(heights)  - pop_i
            mx_a = max(mx_a, base * pop_h)
        
        return mx_a


            