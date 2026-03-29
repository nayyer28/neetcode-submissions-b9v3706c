class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        starts = []
        for n in hset:
            if n-1 not in hset:
                starts.append(n)
        mx = 0
        for s in starts:
            l = 0
            while s + l in hset:
                if l+1 > mx:
                    mx = l+1
                l += 1
        return mx