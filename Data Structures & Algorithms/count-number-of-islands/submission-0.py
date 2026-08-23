class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs from the 1s.

        

        ROWS = len(grid)
        COLS = len(grid[0])
        processed = set()

        def dfs(row: int, col: int):
            if grid[row][col] == "0":
                return
            if (row, col) in processed:
                return
            processed.add((row, col))
            
            if row + 1 < ROWS:
                dfs(row+1, col)
            if row - 1 >= 0:
                dfs(row - 1, col)
            if col + 1 < COLS:
                dfs(row, col + 1)
            if col - 1 >= 0:
                dfs(row, col - 1)
            

        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "0":
                    continue
                if (i,j) in processed:
                    continue
                islands += 1
                dfs(i, j)
        return islands
                
