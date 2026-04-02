class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        def helper (values, i):
            if i == len (nums):
                ret.append (values[::])
                return 

            values.append (nums [i])
            helper (values, i+1)

            values.pop()

            while i != len (nums)-1 and nums [i] == nums [i+1]:
                i+=1

            helper (values, i+1)

        helper ([],0)

        return ret

        