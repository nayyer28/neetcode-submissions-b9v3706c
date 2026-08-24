class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return -1
        
        ROWS = len(grid)
        COLS = len(grid[0])

        dq = deque([])
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    dq.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        lvl = -1
        while dq:
            nxtq = []
            lvl += 1
            while dq:
                (i,j) = dq.popleft()
                # 4 directions
                if i + 1 < ROWS and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    fresh -= 1
                    nxtq.append((i+1,j))
                if j + 1 < COLS and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    fresh -= 1
                    nxtq.append((i,j+1))
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    fresh -= 1
                    nxtq.append((i-1,j))
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    fresh -= 1
                    nxtq.append((i,j-1))
            dq = deque(nxtq)
        if fresh > 0:
            return -1
        elif lvl > -1:
            return lvl
        else:
            return 0
                
                
                
                
