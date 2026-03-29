class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # abcabc -> axc abc. # abba axb
        def isPalindrome(st: str):
            l, r = 0, len(st) - 1

            while l < r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        res = []
        parts = []

        def dfs(i:int, j: int):
            if j == len(s):
                res.append(parts.copy())
                return
            if i == len(s):
                return
            
            # pick
            if isPalindrome(s[j:i+1]):
                parts.append(s[j:i+1])
                dfs(i+1, i+1)
                parts.pop()
            # skip
            dfs(i+1, j)
        dfs(0,0)
        return res



