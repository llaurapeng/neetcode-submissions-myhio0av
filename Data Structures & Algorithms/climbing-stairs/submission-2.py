class Solution:
    def climbStairs(self, n: int) -> int:
        self.ret = 0 
        def helper (step):
            if step == n: 
                self.ret+=1
                return 

            if step > n: 
                return

            helper (step + 1)

            helper (step + 2)

        helper (0)

        return self.ret
