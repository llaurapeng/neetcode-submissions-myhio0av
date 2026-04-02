class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        r = len (heights) - 1
        ret = 0

        while l < r: 
            minVal = min (heights [l], heights [r]) * (r - l)
            ret = max (ret, minVal)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ret
        