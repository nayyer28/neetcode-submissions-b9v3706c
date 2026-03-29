class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        mx_prefix = float("-inf")
        for i, h in enumerate(height):      
            prefix[i] = mx_prefix
            if mx_prefix < h:
                mx_prefix = h
        mx_suffix = float("-inf")
        for i in range(len(height)-1,-1,-1):      
            suffix[i] = mx_suffix
            if mx_suffix < height[i]:
                mx_suffix = height[i]
        print(prefix, suffix)

        water = 0
        for i, h in enumerate(height):
            water += max( min( prefix[i],suffix[i] ) - h, 0)

        return water

            