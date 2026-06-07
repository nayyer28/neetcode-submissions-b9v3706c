class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charPos = {}

        left, right = 0, 0
        mx = float("-inf")
        while right < len(s):
            char = s[right]

            if char in charPos and charPos[char] >= left:
                mx = max(mx, right - left) # right already at dupe - so no need of +1
                left = charPos[char] + 1
            
            charPos[char] = right
                
            right += 1
        
        return max(mx, right - left) # right already at len(s) so no need of +1

            