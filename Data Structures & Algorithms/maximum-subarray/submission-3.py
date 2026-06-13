class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #     [2,-3,4,-5,2,1,-1,3]
        # sum  2 -1 3 -2 0 1 0 3
        # res. 2  0 4  0 0 1 0 3

        #     [-2,-3,-4]
        # sum   
        # res. 

        s = 0
        mx = float("-inf")
        cut_off = 0
        for n in nums:
            s += n
            mx = max(mx, s - cut_off)
            cut_off = min(cut_off, s)
            
        
        return mx

