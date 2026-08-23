class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        processed = set()
        # dfs from the 1s.
        def dfs(row: int, col: int) -> int:
            if grid[row][col] == 0:
                return 0
            if (row, col) in processed:
                return 0
            processed.add((row, col))
            
            me = 1

            if row + 1 < ROWS:
                me += dfs(row+1, col)
            if row - 1 >= 0:
                me += dfs(row - 1, col)
            if col + 1 < COLS:
                me += dfs(row, col + 1)
            if col - 1 >= 0:
                me += dfs(row, col - 1)
            
            return me
            

        area = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    continue
                if (i,j) in processed:
                    continue
                # new island
                area = max(area,dfs(i, j))
        return area