class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 3->3->3->1->3
        # 0  1  2  3  4

        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = nums[0]

        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow
