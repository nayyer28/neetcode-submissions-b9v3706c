class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = 1
        mn = 1
        res = float("-inf")
        for n in nums:
            old_mx = mx
            mx = max(n, mx * n, mn * n) # max = new subarray starting at i, mx * n or mn * n.
            # not mx since:
            # if n is neg and mx is pos - mx * n is less than n
            mn = min(n, mn * n, old_mx * n) # min is either n or mn * n or mx * n

            res = max(mx, res)
        return res