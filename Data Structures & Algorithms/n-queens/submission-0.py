class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        rows = set()
        cols = set()
        ldiags = set() # row + col
        rdiags = set() # col - row

        def isSafe(i:int, j :int):
            # row safe
            if i in rows:
                return False
            # col safe
            if j in cols:
                return False
            # ldiag safe
            if i + j in ldiags:
                return False
            # rdiag safe
            if j - i in rdiags:
                return False
            return True

        res = []

        def dfs(i:int,j:int):
            if i == n: # # you have a legit solution
                res.append(["".join(row) for row in board])
                return
            if j == n: # we are out of bounds
                return
            
            # pick isSafe
            if isSafe(i,j):
                board[i][j] = "Q"
                rows.add(i)
                cols.add(j)
                ldiags.add(i+j)
                rdiags.add(j-i)
                dfs(i+1,0)
                board[i][j] = "."
                rows.remove(i)
                cols.remove(j)
                ldiags.remove(i+j)
                rdiags.remove(j-i)
            
            dfs(i,j+1)
        dfs(0,0)
        return res
