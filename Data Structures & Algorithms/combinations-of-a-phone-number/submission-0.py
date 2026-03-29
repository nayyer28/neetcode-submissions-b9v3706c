class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
                }
        
        res = []

        def dfs(i:int, curr: str):
            if i == len(digits):
                if curr:
                    res.append(curr)
                return
            
            for c in hmap[digits[i]]:
                # pick c
                dfs(i+1,curr + c)
                #skip c
        dfs(0, "")
        return res
            
            