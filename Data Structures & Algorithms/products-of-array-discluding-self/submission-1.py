class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # need two prefix calculations

        pre, suf = [1] * len(nums), [1] * len(nums)

        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        
        res = []

        for p, s in zip(pre,suf):
            res.append(p*s)
        
        return res

        