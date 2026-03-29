class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i:int, t:int):
            if t < 0:
                return
            if t == 0:
                res.append(subset.copy())
                return
            
            if i < len(candidates):
                subset.append(candidates[i])
                dfs(i, t - candidates[i])
                subset.pop()
                dfs(i+1,t)
        dfs(0,target)
        return res