import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ret = float ('inf')

        l, r = 1, max (piles)

        while l <= r: 
            totalhours = 0 
            mid = (l+r)//2
            print (mid)
            for pile in piles: 
                totalhours+= math.ceil (pile/mid)

            if totalhours <= h: 
                ret = min (ret, mid)
                r = mid - 1
            else: #totalhours > h need to look at smaller values
                l = mid + 1

        return ret






