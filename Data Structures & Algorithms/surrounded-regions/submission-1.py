class Solution:
    def solve(self, board: List[List[str]]) -> None:

        visit = set()
        direction = [[-1,0],[0,-1],[0,1],[1,0]]


        rows, cols = len (board), len (board [0])

        def bfs (r,c):
            q = deque([])
            q.append ((r,c))
            inSame = [(r,c)]
            visit.add ((r,c))

            while q: 
                row, col = q.popleft()

                for dr, dc in direction: 
                    newr = dr + row
                    newc = dc + col

                    if (
                        newr in range (rows) and 
                        newc in range (cols) and
                        (newr, newc) not in visit and 
                        board [newr][newc] == "O"
                    ):
                        inSame.append ((newr,newc))
                        q.append ((newr,newc))
                        visit.add ((newr,newc))

            #return a list of tuples of the places that are in the same region
            return inSame


        for r in range (rows):
            for c in range (cols):
                
                if board [r][c] == "O" and (r,c) not in visit: 
                    together = bfs (r,c)    
                    print (together)
                    switch = True
                    for row, col in together: 
                        for dr, dc in direction: 
                            newr = row + dr
                            newc = col + dc

                            #False if we reach a O and it is not part of togehter
                            #False if we out of bounds

                            if (
                                newr not in range (rows) or
                                newc not in range (cols) or 
                                (board[newr][newc] == "O" and (newr,newc) not in together)
                            ):
                                switch = False

                    if switch == True: 
                        for row, col in together: 
                            board [row][col] = "X"

        return 


