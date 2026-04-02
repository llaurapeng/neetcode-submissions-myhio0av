class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cols, rows = len (grid [0]), len (grid)
        time = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque ()
        fresh = 0

        #output need 0 fresh fruit at the end

        #count how many fresh fruit

        for r in range (rows):
            for c in range (cols):
                if grid [r][c] == 1: 
                    fresh+=1
                if grid [r][c] == 2: 
                    q.append ((r,c))

        while fresh > 0 and q: 
            length = len (q)
            for i in range (length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r+ dr
                    col = c + dc
                    if (row in range (rows) and 
                        col in range (cols) and 
                        grid [row][col] == 1):
                        fresh-=1
                        grid [row][col] = 2
                        q.append ((row, col))
            time+=1

        if fresh == 0: 
            return time
        else: 
            return -1















            