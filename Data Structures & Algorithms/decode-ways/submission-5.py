class Solution:
    def numDecodings(self, s: str) -> int:
        # dp - tabulation - O(n) time with O(1) space where n = len(s)
        prev2 = 1
        prev1 = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            curr = 0

            if s[i - 1] != "0":
                curr += prev1

            if 10 <= int(s[i - 2:i]) <= 26:
                curr += prev2

            prev2 = prev1
            prev1 = curr

        return prev1
