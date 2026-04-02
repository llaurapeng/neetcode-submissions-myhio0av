class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #1. on the boarders find the values with O

        from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        
        def dfs(r, c):
            # Initialize the queue with the starting point
            q = deque([(r, c)])
            # Mark the starting cell as visited ('t')
            board[r][c] = 't'
            
            while q:
                row, col = q.popleft()
                
                # Explore all four directions
                for dr, dc in directions:
                    newr, newc = row + dr, col + dc
                    
                    # Ensure we're within bounds and the cell is an "O"
                    if 0 <= newr < rows and 0 <= newc < cols and board[newr][newc] == "O":
                        # Mark the cell as visited and add to the queue
                        board[newr][newc] = 't'
                        q.append((newr, newc))
        
        # Step 1: Start DFS from all "O" cells on the borders
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)  # Top row
            if board[rows-1][c] == "O":
                dfs(rows-1, c)  # Bottom row
        
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)  # Left column
            if board[r][cols-1] == "O":
                dfs(r, cols-1)  # Right column

        # Step 2: Convert "O" to "X" and "t" back to "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "t":
                    board[r][c] = "O"





        

