class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hmap = {}

        for n in nums:
            hmap[n] = hmap.get(n,0) + 1

        for nu, co in hmap.items():
            if co == 1:
                return nu