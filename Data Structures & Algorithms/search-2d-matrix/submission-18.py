class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, col = len (matrix), len (matrix [0])
        currow = 0

        #check to see which row value in

        for i in range (rows):
            
            if matrix [i][col-1] < target:
                #needs a greater value
                currow+=1

        if currow >= rows: 
            print (currow)
            return False

        l, r = 0, col - 1
        while l <= r:
            midind =  l + (r - l) // 2
            mid = matrix [currow][midind]

            if mid < target: 
                #need bigger values

                l = midind + 1
            elif mid > target:
                #need smaller values
                r = midind -1

            else: 
                return True

        return False


