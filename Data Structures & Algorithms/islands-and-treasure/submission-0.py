class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        '''

        1.find all the land cells and put into a list
        2.loop through each land cell and go through every direction to find
        a treasure chest (O)

        '''



        lands = []

        rows, cols = len (grid), len (grid[0])

        for r in range (rows): 
            for c in range (cols): 
                if grid [r][c] == 2147483647:
                    #found a land cell
                    lands.append ((r, c))

        def explore (r, c):
            visit = set()
            visit.add ((r,c))
            q = deque ([(r,c,0)])
            directions = [[1,0],[0,1],[-1,0], [0,-1]]
            steps = 0
            found = False
            while q: 
                row, col, steps = q.popleft()
      
                for dr, dc in directions: 
                    newr = row  + dr
                    newc = col + dc

                    if (newr in range (rows) and 
                        newc in range (cols) and 
                        (newr, newc) not in visit):
                            if grid [newr][newc] == 0:
                                found = True
                                
                                return steps + 1

                    
                            if grid [newr][newc] != -1: 
                                q.append ((newr, newc, steps + 1))
                                visit.add ((newr, newc))
                
            return 2147483647


        for r,c in lands: 
            grid [r][c] = explore (r,c)




        