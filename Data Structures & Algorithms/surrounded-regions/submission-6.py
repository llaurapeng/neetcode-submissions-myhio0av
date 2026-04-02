class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #1. on the boarders find the values with O
        rows, cols = len(board), len(board[0])
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        
        def dfs(r, c):
            # Stack or queue for DFS
            q = deque([(r, c)])
            while q:
                row, col = q.popleft()
                # Mark this cell as visited (temporary mark 't')
                board[row][col] = 't'
                
                for dr, dc in directions:
                    newr, newc = row + dr, col + dc
                    
                    # Check bounds and whether it's an "O" that hasn't been visited yet
                    if 0 <= newr < rows and 0 <= newc < cols and board[newr][newc] == "O":
                        board[newr][newc] = 't'  # Mark it immediately to avoid revisiting
                        q.append((newr, newc))
        
        # Step 1: Start DFS from boundary 'O' cells
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows-1][c] == "O":
                dfs(rows-1, c)
        
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols-1] == "O":
                dfs(r, cols-1)
        
        # Step 2: Change "O" to "X" and "t" back to "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "t":
                    board[r][c] = "O"