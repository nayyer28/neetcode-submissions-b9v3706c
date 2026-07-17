class Solution:
    def trap(self, height: List[int]) -> int:
        # single pass

        prefix = [0] * len(height)
        pmx = 0
        suffix = [0] * len(height)
        smx = 0

        left , right = 0, len(height) - 1

        while left < len(height):
            prefix[left] = pmx
            pmx = max(pmx, height[left])
            suffix[right] = smx
            smx = max(smx, height[right])
            left += 1
            right -= 1
        
        res = 0
        for i in range(len(prefix)):
            res += max(min(prefix[i], suffix[i]) - height[i], 0)

        return res
