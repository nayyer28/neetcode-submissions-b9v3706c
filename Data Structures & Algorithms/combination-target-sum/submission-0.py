class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        combos = set()

        def dfs(t: int):
            if t == 0:
                key = tuple(sorted(subset))
                if key not in combos:
                    res.append(subset.copy())
                    combos.add(key)
            
            for n in nums:
                if t >= n:
                    subset.append(n)
                    dfs(t-n)
                    subset.pop()
        dfs(target)
        return res

                