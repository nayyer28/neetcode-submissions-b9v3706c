class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # [9,2,2,4,6,1,5], target = 8
        # if you skip an element you skip all occurences of it later

        res = []
        subset = []
        skipped = set()
        def dfs(i:int, t: target):
            if t == 0:
                res.append(subset.copy())
                return
            if t < 0 or i >= len(candidates):
                return
            
            if candidates[i] not in skipped: # normal take and skip decision
                # take it
                subset.append(candidates[i])
                dfs(i+1,t-candidates[i])
                subset.pop()
                # skip it
                skipped.add(candidates[i])
                dfs(i+1,t)
                skipped.remove(candidates[i])
            else: # force skip
                dfs(i+1,t)
                

        dfs(0,target)
        return res
            

