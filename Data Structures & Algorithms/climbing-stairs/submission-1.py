class Solution:
    def climbStairs(self, n: int) -> int:

        self.ret = 0


        def helper (currStep):
            if currStep == n: 
                self.ret+=1
                return

            if currStep > n: 
                return

            helper (currStep + 1)

            helper (currStep +2)


        helper (0)
        return self.ret
            
        