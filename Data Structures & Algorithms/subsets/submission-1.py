class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.ret = []

        def helper (dex, res): 
            if dex >= len (nums):
                self.ret.append (res.copy())
                return

            res.append (nums [dex])
            helper (dex+1, res)

            res.pop()

            helper (dex+1, res)

        helper (0,[])

        return self.ret

        