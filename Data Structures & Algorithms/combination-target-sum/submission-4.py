class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        ret = []

        def helper (i, vals, total):

            if i >= len (nums) or total > target:
                return 
            if total == target: 
                ret.append (vals.copy())
                return

            vals.append (nums [i])
            helper (i, vals, total + nums [i])
            vals.pop()
            helper (i+1, vals, total)

        helper (0, [],0)

        return ret