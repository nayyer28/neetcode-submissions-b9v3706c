class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # sorted unrotated array
        if nums[0] < nums[-1]:
            return nums[0]

        # sorted rotated array:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # find in the left
                right = mid
            else:
                # find in the left
                left = mid + 1

        return nums[mid]
