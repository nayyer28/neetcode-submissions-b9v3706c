class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                if nums[mid] <= nums[right] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] >= nums[left] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 51234. 23451
        return -1
