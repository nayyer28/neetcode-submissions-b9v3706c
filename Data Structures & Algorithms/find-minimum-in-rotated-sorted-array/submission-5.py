class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1 # Im certain curent mid is not minimum so +1
            elif nums[mid] < nums[right]:
                right = mid # current mid could possibly be the minimum so no +1
            else:
                return nums[mid]
            
        
            
                
                