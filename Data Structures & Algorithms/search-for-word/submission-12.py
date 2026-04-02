class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        col, row = len (board[0]), len (board)
        dire = [[-1, 0],[1,0], [0,-1],[0,1]]
        seen = []
        def help (r, c, i):

            if (r not in range (row) or 
                c not in range (col) or
                board [r][c] != word [i] or 
                [r,c] in seen):
                return False
            if board [r][c] == word [i] and i == len (word)-1: 
                return True

            seen.append ([r,c])

            res = (help (r+1, c, i+1) or 
                    help (r-1,c, i+1) or
                    help (r, c+1, i+1) or 
                    help (r, c-1, i+1))

            seen.remove ([r,c])

            return res


        for r in range (row):
            for c in range (col):
                if help (r,c, 0):
                    return True

        return False



       