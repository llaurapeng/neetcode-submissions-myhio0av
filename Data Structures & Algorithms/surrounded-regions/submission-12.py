class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #1. on the boarders find the values with O

        rows, cols  = len (board), len (board [0])
        directions = [[-1,0],[0,-1], [0,1], [1,0]]


        def dfs (r,c):
            q = deque ([])
            q.append ((r,c))
            board [r][c] = "t"
            
            while q: 
                row, col = q.popleft ()


                for dr, dc in directions:
                    newr = row + dr
                    newc = col + dc

                    if 0 <= newr < rows and 0 <= newc < cols and board[newr][newc] == "O":
                        # Mark the cell as visited and add to the queue
                        board[newr][newc] = 't'
                        q.append((newr, newc))
        

        for c in range (cols):
            if board [0][c] == "O":
                dfs (0,c)

            if board [rows-1][c] == "O":
                dfs (rows-1,c)

        for r in range (rows):
            if board [r][0] == "O":
                dfs (r,0)
            if board [r][cols-1] == "O":
                dfs (r,cols-1)

        

        for r in range (rows):
            for c in range (cols):
                if board [r][c] == "O":
                    board [r][c] = "X"
                if board [r][c] == "t":
                    board [r][c] = "O"

        return 




        

