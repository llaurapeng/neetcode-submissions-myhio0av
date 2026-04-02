class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def solution (l, r, column):

            if column > len (matrix)-1:
                return False

            middle = (l+r)//2
            middleVal = matrix [column][middle] 
 

            if middleVal == target: 
                print (1)
                return True
            if l > r: 
                print (2)
                return False
            if l == r and matrix [column][l] != target and len (matrix) == 0:
                print (3)
                return False 
            if matrix [column][r] < target: 
                return solution (l, r, column+1)
            elif middleVal > target: 
                return solution (l,r-1, column)
            elif middleVal < target: 
                return solution (l+1, r,column)

        
        ret = solution (0, len (matrix[0])-1, 0)

        return ret


