class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = 0 
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        time = 0

        q = deque ([])
        rows, cols = len (grid), len (grid [0])

        for r in range (rows): 
            for c in range (cols): 
                if grid [r][c] == 1: 
                    fresh+=1
                if grid[r][c] == 2: 
                    q.append ((r,c))


        while q and fresh > 0: 
            rottens_n = len (q)

            #explore from every rotten area and mark as rotten and add to q
            for i in range (rottens_n):
                row,col = q.popleft()
                for dr, dc in directions: 
                    new_row = row + dr
                    new_col = col + dc

                    if (new_row in range (rows) and
                    new_col in range (cols) and
                    grid[new_row][new_col] == 1
                    ):
                        fresh-=1
                        grid[new_row][new_col] = 2
                        q.append ((new_row, new_col))
            time+=1
        return time if fresh == 0 else -1







