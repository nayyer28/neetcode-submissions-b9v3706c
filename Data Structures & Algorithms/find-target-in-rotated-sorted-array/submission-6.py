class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            # left sorted
            if nums[left] <= nums[mid]:

                if target < nums[mid] and target < nums[left] or target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid] and target >= nums[left]:
                    right = mid - 1
            # right sorted
            else:
                if target > nums[mid] and target > nums[right] or target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid] and target <= nums[right]:
                    left = mid + 1
        return -1
