class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        visit = set ()
        q = deque ([])
        ret = 0

        rows, cols = len (grid), len (grid[0])

        def bfs (r, c): 
            islands = 1

            visit.add ((r, c))
            q.append ((r, c))

            while q: 
                row, col = q.popleft()

                for dr, dc in directions: 
                    new_r, new_c = row + dr, col + dc  # New row and column after moving in the direction

                    # Check if the new position is within bounds and is land
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1 and (new_r, new_c) not in visit:
                        islands += 1  # Increase island area count
                        visit.add((new_r, new_c))  # Mark this cell as visited
                        q.append((new_r, new_c)) 

            return islands

        for r in range (rows):
            for c in range (cols):
                if (grid [r][c] == 1 and (r,c) not in visit):
                    ret = max (ret, bfs (r, c))


        return ret
