class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ret = float ('inf')
        summ = 0
        for r in range (len (nums)):
            summ+= nums [r]
                #increment left pointer
            while l <= r and summ >= target: 
                ret = min (ret, r-l + 1)
                summ = summ - nums [l]
                l+=1

        if ret == float ('inf'):
            return 0
        return ret

