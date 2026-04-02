class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len (nums) 
        post = [0] * len (nums)
        ret = [0] * len (nums)
        for i, x in enumerate (nums): 
            # look at what's before and take the sum and mulitply to it

            if i == 0: 
                pre[i] = x
            else: 
                pre [i] = pre [i-1] * x

        for i in range (len (nums) -1, -1 ,-1):
            if i == len (nums) -1: 
                post [i] = nums [i]
            else: 
                post [i] = post [i+1] * nums[i]

        
        for ind, val in enumerate (nums): 
            if ind == 0: 
                ret [ind] = post [ind + 1]

            elif ind == len (nums) -1: 
                ret [ind] = pre [ind -1]
            else: 
                ret [ind] = pre [ind-1] * post [ind+1]

        return ret
        


            
