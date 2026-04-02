class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs (i, sums, values):
            if sums > target: 
                return 
            if sums == target: 
                res.append (values[:])
                return 
            if i >= len (nums):
                return 

            values.append (nums [i])
            dfs (i, sums + nums [i], values)

            values.pop ()

            dfs (i+1, sums, values)


        dfs (0, 0,[])

        return res

