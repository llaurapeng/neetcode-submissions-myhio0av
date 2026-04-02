class Solution:
    def rob(self, nums: List[int]) -> int:

        #dp[i] = the max cost of from 1 to index i
        dp = [0] * (len (nums)+1)
        dp [0] = 0
        dp[1] = nums [0]
        for ind,cost in enumerate (nums[1:], start = 2):
            #include cost
            cost1 = cost + dp [ind-2]
            #not include cost
            cost2 = dp[ind-1]
            dp [ind] = max (cost1,cost2)
           
        print (dp)
        return max (dp)