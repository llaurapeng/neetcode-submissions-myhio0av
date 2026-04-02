class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []

        for x in range (len (nums)):
            newLi = nums.copy()
            newLi.pop (x)
            print (newLi)
            product = 1
            for y in newLi: 
                product*= y
            ret.append (product)
        return ret
