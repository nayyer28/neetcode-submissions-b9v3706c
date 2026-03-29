class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(i:int, j:int, nxt: int) -> bool:

            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return False
            print(i,j)
            c = board[i][j]

            if c == '#' or c!= word[nxt]:
                return False
            
            if nxt == len(word) - 1:
                return True
            
            board[i][j] = '#'
            nxt += 1
            # look left
            l = dfs(i,j-1, nxt)
            # look right
            r = dfs(i,j+1, nxt)
            # look up
            u = dfs(i-1, j, nxt)
            # look down
            d = dfs(i+1,j,nxt)
            board[i][j] = c
            return l or r or u or d
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        return False
        
        


            


            


            