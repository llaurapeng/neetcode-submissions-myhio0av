class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ret = []

        def helper (sum, values, i): 
            if sum == target: 
                ret.append (values.copy())
                return 
            if sum > target: 
                return 
            if i >= len (nums): 
                return

            values.append (nums [i])
            helper (sum + nums [i], values, i)

            values.pop()
            helper (sum, values, i+1)

        helper (0,[],0)

        return ret

