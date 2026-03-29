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
                    #nxt = chosen[:]
                    chosen[i] = True
                    dfs(chosen)
                    perm.pop()
                    chosen[i] = False
        dfs([False] * len(nums))
        return res

            
            
