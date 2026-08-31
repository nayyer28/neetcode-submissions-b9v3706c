class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R = len(heights)
        C = len(heights[0])

        pac = set()
        pq = deque([])
        for j in range(C):
            pq.append((0,j))
            pac.add((0,j))
        for i in range(1,R):
            pq.append((i,0))
            pac.add((i,0))
        
        while pq:
            nxtpq = []
            while pq:
                (i,j) = pq.popleft()
                # check 4 directions:
                if i + 1 < R and (i+1,j) not in pac and heights[i][j] <= heights[i+1][j]:
                    nxtpq.append((i+1,j))
                    pac.add((i+1,j))
                if i - 1 >= 0 and (i - 1) not in pac and heights[i][j] <= heights[i-1][j]:
                    nxtpq.append((i-1,j))
                    pac.add((i-1,j))
                if j + 1 < C and (i, j + 1) not in pac and heights[i][j] <= heights[i][j+1]:
                    nxtpq.append((i,j+1))
                    pac.add((i,j+1))
                if j - 1 >= 0 and (i, j-1) not in pac and heights[i][j] <= heights[i][j-1]:
                    nxtpq.append((i,j-1))
                    pac.add((i,j-1))
            pq = deque(nxtpq)
        # [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]
        atl = set()
        aq = deque([])
        for j in range(C):
            aq.append((R-1,j))
            atl.add((R-1,j))
        for i in range(R-1):
            aq.append((i,C-1))
            atl.add((i,C-1))
        
        while aq:
            nxtaq = []
            while aq:
                (i,j) = aq.popleft()
                # check 4 directions:
                if i + 1 < R and (i+1,j) not in atl and heights[i][j] <= heights[i+1][j]:
                    nxtaq.append((i+1,j))
                    atl.add((i+1,j))
                if i - 1 >= 0 and (i - 1) not in atl and  heights[i][j] <= heights[i-1][j]:
                    nxtaq.append((i-1,j))
                    atl.add((i-1,j))
                if j + 1 < C and (i, j + 1) not in atl and heights[i][j] <= heights[i][j+1]:
                    nxtaq.append((i,j+1))
                    atl.add((i,j+1))
                if j - 1 >= 0 and (i, j-1) not in atl and heights[i][j] <= heights[i][j-1]:
                    nxtaq.append((i,j-1))
                    atl.add((i,j-1))
            aq = deque(nxtaq)
        
        res = []

        for (i,j) in pac:
            if (i,j) in atl:
                res.append([i,j])
        return res

            
