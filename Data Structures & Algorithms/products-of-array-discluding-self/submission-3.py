class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #pre [i] = product of everything from 0 to i
        #after [i] = product of everything after i

        pre = [0] * len (nums)
        pre [0] = nums [0]
        for ind in range (1, len (nums)):
            pre [ind] = pre [ind-1] * nums [ind]

        print (pre)
        after = [0] * len (nums)
        after [len (nums)-1] = nums [len (nums)-1]

        for ind in range (len (nums)-2, -1, -1):
            after [ind] = after [ind+1] * nums [ind]

        print (after)
        ret = []
        ret.append (after [1])

        for ind, num in enumerate (nums[1:], start = 1): 
            ret.append (pre [ind-1]* (after [ind+1] if ind + 1 < len (nums) else 1))

        return ret



            

