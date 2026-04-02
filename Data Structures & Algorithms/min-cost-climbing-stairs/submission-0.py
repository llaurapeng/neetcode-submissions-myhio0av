class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #dp[i] = the min cost to get to step i
        dp = [0] * (len (cost))
        
        dp [0] = cost [0]
        dp [1] = cost [1]

        for ind, stair in enumerate (cost[2:], start = 2): 
            cost = stair + min (dp [ind-1], dp [ind-2])
            dp [ind] = cost

        return min (dp [-1], dp [-2])
                

