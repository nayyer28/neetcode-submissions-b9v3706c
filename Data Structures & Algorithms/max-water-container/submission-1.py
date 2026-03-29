class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights) - 1
        mx = float("-inf")
        while l < r:
            mx = max(mx, min(heights[r],heights[l]) * (r-l))
            if min(heights[r],heights[l]) == heights[r]:
                r -= 1
            else:
                l += 1
        return mx