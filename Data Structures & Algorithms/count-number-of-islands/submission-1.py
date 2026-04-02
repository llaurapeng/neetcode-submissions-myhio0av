class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols, rows = len (grid [0]), len (grid)

        visit = []

        ret = 0
        directions = [[-1,0], [1,0], [0,1],[0,-1]]

        def helper (row, col):
            explore = deque ([[row,col]])

            while explore: 
                curr_row, curr_col = explore.popleft ()
                visit.append ([curr_row,curr_col])

                for dr, dc in directions: 
                    new_row = curr_row + dr
                    new_col = curr_col + dc

                    if (new_row in range (rows) and
                        new_col in range (cols) and
                        grid [new_row][new_col] == "1" and 
                        [new_row, new_col] not in visit):
                        explore.append ([new_row, new_col])


        for r in range (rows):
            for c in range (cols):
                if grid [r][c] == "1" and [r,c] not in visit:
                    #start exploring from this cell
                    helper (r, c)
                    ret+=1

        return ret
        