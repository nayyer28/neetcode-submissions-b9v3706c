class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []


        def dfs(chosen:List[bool]):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(chosen)):
                if not chosen[i]:
                    perm.append(nums[i])
                    nxt = chosen[:]
                    nxt[i] = True
                    dfs(nxt)
                    perm.pop()
        dfs([False] * len(nums))
        return res

            
            
