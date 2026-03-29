class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        # [1,2,3,4,5]
        def dfs(i:int,t:int):
            if t == 0:
                res.append(subset.copy())
                return
            if t < 0 or i >= len(candidates):
                return
            # take
            subset.append(candidates[i])
            dfs(i+1, t-candidates[i])
            # skip
            subset.pop()
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            dfs(i, t)


        dfs(0, target)
        return res