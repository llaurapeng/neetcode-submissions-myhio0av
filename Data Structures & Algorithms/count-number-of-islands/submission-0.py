class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

       # Empty grid case
        if not grid or not grid[0]: 
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()  # To keep track of visited cells
        islands = 0

        # BFS function to explore all connected land cells
        def bfs(r, c):
            visited.add((r, c))
            q = deque([(r, c)])  # Start BFS from the given cell

            # Directions to explore the neighbors (up, down, left, right)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while q:
                r, c = q.popleft()
                # Explore all 4 possible directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        # Iterate over each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # Found an unvisited land cell, start BFS to mark the island
                    bfs(r, c)
                    islands += 1  # Increment island count

        return islands