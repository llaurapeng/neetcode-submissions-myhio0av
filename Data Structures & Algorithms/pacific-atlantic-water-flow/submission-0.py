class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len (heights), len (heights [0])
        directions = [[-1,0],[0,-1], [0,1],[1,0]]
        ret = []

        for r in range(rows): 
            for c in range(cols): 
                pacific = False
                atlantic = False
                visited = set() 
                q = deque()
                q.append((r, c))
                visited.add((r, c))

                while q: 
                    row, col = q.popleft()

                    if row == 0 or col == 0:
                        pacific = True
                    if row == rows - 1 or col == cols - 1:
                        atlantic = True

                    if pacific and atlantic:
                        ret.append([r, c])
                        break  # No need to continue searching from this cell

                    for dr, dc in directions: 
                        newr = row + dr
                        newc = col + dc

                        if (0 <= newr < rows and 
                            0 <= newc < cols and 
                            (newr, newc) not in visited and 
                            heights[newr][newc] <= heights[row][col]):
                            
                            q.append((newr, newc))
                            visited.add((newr, newc))

        return ret