class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hset = set(nums)
        starts = []
        for n in nums:
            if not n-1 in hset:
                starts.append(n)
        
        mx_l = 1
        for s in starts:
            look_for = s + 1
            l = 1
            while look_for in hset:
                l += 1
                look_for += 1
            if l > mx_l:
                mx_l = l
            
        return mx_l