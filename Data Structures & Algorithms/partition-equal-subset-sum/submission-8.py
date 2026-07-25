class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # hashset
        # can we make j sum having seen all n's so far
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        sums = set()

        for n in nums:
            nxtSums = set()
            for s in sums:
               nxtSums.add(s)
               nxtSums.add(s + n)
            nxtSums.add(n)
            sums = nxtSums
            if target in sums:
                return True
        return False