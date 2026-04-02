class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max (piles)
        l = 1

        ret = 0

        while l <= r:
            mid = (l + r)//2
            hours = 0
            for x in piles: 
                hours += math.ceil (x/mid)

            if hours <=  h: 
                #need bigger dividers
                #need to increment l 
                r = mid - 1
                ret = mid

            elif hours > h: 
                l = mid + 1
  

        return ret


            


        