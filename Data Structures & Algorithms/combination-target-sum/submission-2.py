class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i:int, t:int):
            if t == 0:
                res.append(subset.copy())
                return
            if t < 0 or i >= len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(i, t - candidates[i])
            subset.pop()
            dfs(i+1,t)
        dfs(0,target)
        return res