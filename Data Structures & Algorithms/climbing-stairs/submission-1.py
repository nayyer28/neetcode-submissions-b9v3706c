class Solution:
    def climbStairs(self, n: int) -> int:
        # memoization
        n2Ways = {}
        def dfs(k: int) -> int:
            nonlocal n2Ways
            if k < 0:
                return 0
            if k == 0:
                return 1
            if k not in n2Ways:
                n2Ways[k] = dfs(k-1) + dfs(k-2)
            return n2Ways[k]
        return dfs(n)

