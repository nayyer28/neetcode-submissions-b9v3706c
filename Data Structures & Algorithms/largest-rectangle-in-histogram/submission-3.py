class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        mx_a = 0
        heights.append(0)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                pop_h, pop_i = stack.pop()
                base = i - pop_i
                mx_a = max(mx_a, base * pop_h)
                start = pop_i
            #if stack and stack[-1][0] == h: # optional - same height in succession doesnt cover a new rectangle. they basically cut a smaller section of the larger rectangle
            #    continue
            stack.append((h, start))
        
        #while stack:
        #    pop_h, pop_i = stack.pop()
        #    base = len(heights)  - pop_i
        #    mx_a = max(mx_a, base * pop_h)
        
        return mx_a


            