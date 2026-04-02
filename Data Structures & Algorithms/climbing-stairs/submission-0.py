class Solution:
    def climbStairs(self, n: int) -> int:

        self.ret= 0
        def dfs (steps):

            if steps >= n: 
                if steps == n: 
                    self.ret+=1
                return 

            dfs (steps + 1) #using one step

            dfs (steps + 2)

        dfs (0)

        return self.ret


        