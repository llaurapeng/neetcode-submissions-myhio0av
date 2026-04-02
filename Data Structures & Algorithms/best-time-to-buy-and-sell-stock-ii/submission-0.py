class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        ret = 0
        #BUY LOW SELL HIGH
        #left pointer keeps track of the min value

        #right pointer keeps track of the max value

        for r in range (len (prices)):
            if prices [r] < prices [l]:
                l = r

            if prices [r] > prices [l]:
                ret+= prices [r] - prices [l]
                l = r

            r+=1
        
        return ret



        