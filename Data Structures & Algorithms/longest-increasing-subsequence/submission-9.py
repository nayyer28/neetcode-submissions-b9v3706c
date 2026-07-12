class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # binary search solution
        # [9, 1, 4, 2, 3, 3, 7]
        # 1 2 3 7 
        dp = [nums[0]]

        for i in range(1,len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                continue
            
            left , right = 0, len(dp) - 1
            pos = -1
            
            while left <= right:
                mid = (left + right) // 2

                if dp[mid] == nums[i]:
                    pos = mid
                    break
                elif dp[mid] > nums[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            if pos == -1:
                pos = left

            dp[pos] = nums[i]

        return len(dp)

        