class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        mx_area = float("-inf")
        while left < right:
            m = min(heights[left], heights[right])
            area = m * ( right - left )
            if mx_area < area:
                mx_area = area
            
            if heights[left] == m:
                left += 1
            else:
                right -= 1
            
        return mx_area

            