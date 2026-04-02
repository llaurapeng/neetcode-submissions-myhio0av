class Solution:
    def maxProduct(self, nums: List[int]) -> int: 

        #output: return the highest product
        res = nums [0]
        curMin, curMax = 1, 1

        for dex in range (len (nums)):
            
            val1 = nums [dex] * curMax
            val2 = nums [dex] * curMin

            curMin = min (val1, val2, nums [dex])
            curMax = max (val1, val2, nums [dex])

            res = max (res, curMax)

        print (curMin)
        print (curMax)
        return res