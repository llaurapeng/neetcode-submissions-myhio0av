class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len (heights), len (heights [0])
        directions = [[-1,0],[0,-1], [0,1],[1,0]]
        ret = []
        pac, atl = set (), set()

        def dfs (r, c, visit, prevHeight):
            '''
            Base Case
            -when out of bounds
            -result needs to be <= the previous height
            '''

            if (r not in range (rows) or 
                c not in range (cols) or
                heights [r][c] < prevHeight or 
                (r,c) in visit): 
                return

            visit.add ((r, c))

            for dr, dc in directions: 
                dfs (r + dr, c + dc, visit, heights [r][c])


        #pacific rows + atlantic rows

        for i in range (cols):
            dfs (0, i, pac, heights [0][i])
            dfs (rows - 1, i, atl, heights [rows-1][i])

        for i in range (rows):
            dfs (i, 0, pac, heights [i][0])
            dfs (i, cols -1 , atl, heights [i][cols-1])

        res = []

        for r in range (rows):
            for c in range (cols):
                if (r, c) in pac and (r,c) in atl:
                    res.append ([r,c])        

        return res