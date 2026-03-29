class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # open a bracket -> bal + 1 (upto bal <n)
        # close an open bracket  -> bal -1 (only if bal > 1)

        res = []

        def dfs(opn:int, clsd: int, combos: str):
            if opn == n and clsd == n:
                res.append(combos)
                return
           
            # open a bracket
            if opn < n:
                opn += 1
                dfs(opn, clsd, combos + '(')
                opn -= 1
            # close an open bracket
            if clsd < opn:
                clsd += 1
                dfs(opn, clsd, combos + ')')
                clsd -= 1
        dfs(0,0,"")
        return res
            
            
            
            