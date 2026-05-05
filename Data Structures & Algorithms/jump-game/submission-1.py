class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        memo = set()
        
        def canReachFrom(i: int) -> bool:
            nonlocal memo

            if i in memo:
                return False

            if i >= len(nums) - 1:
                return True
            
            for x in range(nums[i], 0, -1):
                nxt = i + x
                if canReachFrom(i + x):
                    return True
            
            memo.add(i)
            return False
        
        return canReachFrom(0)