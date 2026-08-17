class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n) time
        # O(n) space
        s = set()

        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)

        return list(s)[0]