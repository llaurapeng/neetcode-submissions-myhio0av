class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        ret = 0 
        for r in range (len (prices)):
            if prices [l] > prices [r]:
                #increment left
                l = r

            ret = max (ret, prices [r] - prices[l])

        return ret

            
        