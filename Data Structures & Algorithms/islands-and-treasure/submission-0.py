class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        if ROWS == 0:
            return
        COLS = len(grid[0])
        from collections import deque
        queue = deque([])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        seen = set()
        lvl = -1
        while queue:
            nxtqueue = []
            lvl += 1
            while queue:
                (i,j) = queue.popleft()
                if grid[i][j] == -1 or (i,j) in seen:
                    continue
                grid[i][j] = lvl
                seen.add((i,j))
                # navigate all 4 directions
                if i + 1 < ROWS:
                    nxtqueue.append((i+1, j))
                if i - 1 >= 0:
                    nxtqueue.append((i-1,j))
                if j + 1 < COLS:
                    nxtqueue.append((i,j+1))
                if j - 1 >= 0:
                    nxtqueue.append((i,j-1))
            queue = deque(nxtqueue)
        return 
                
               
            
