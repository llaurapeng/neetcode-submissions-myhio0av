class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort ()
        self.ret = []

        def dfs (i, sums):
            if sum (sums) > target or i >= len (nums): 
                return False

            if sum (sums) == target: 
                self.ret.append ((sums.copy()))
                return True

            sums.append (nums [i])
            dfs (i, sums)

            sums.pop()
            dfs (i+1, sums)

        dfs (0, [])

        return self.ret
