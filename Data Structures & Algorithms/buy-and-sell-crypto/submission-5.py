class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        -have a right pointer that incrementes
        - if right p > left p the switch the left pointer to the the right
        '''


        l = 0
        r = 1
        ret = 0

        while r < len (prices):

            if prices [l] > prices [r]:
                l = r
            ret  = max (ret, prices [r] - prices [l])
            r+=1

        return ret

        


