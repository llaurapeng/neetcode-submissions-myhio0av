class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len (heights) -1
        maxScore = 0

        for height in heights: 

            while l < r: 
                if heights[l] <= heights [r]: 
                    tempScore = (r-l) * min (heights[l], heights [r])
                    l+=1

                    maxScore = max (maxScore, tempScore)

                if heights[r] < heights[l]: 
                    tempScore = (r-l) * min (heights[l], heights [r])
                    r-=1
                    maxScore = max (maxScore, tempScore)

        return maxScore

                

        


        