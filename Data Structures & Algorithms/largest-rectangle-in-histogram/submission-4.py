class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # height, start

        mx = float("-inf")

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                p_h, p_start = stack.pop()
                area = p_h * (i - p_start)
                mx = max(mx, area)
                start = p_start
            stack.append((h, start))
        
        while stack:
            p_h, p_start = stack.pop()
            area = p_h * (len(heights) - p_start)
            mx = max(mx, area)
        return mx