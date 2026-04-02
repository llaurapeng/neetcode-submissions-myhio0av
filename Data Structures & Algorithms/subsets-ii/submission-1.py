class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        def helper (vals,i):

            if i >= len (nums):
                ret.append (vals[::])
                return

            
            vals.append (nums [i])
            helper (vals, i+1)

            while i + 1 < len (nums) and nums[i+1] == nums [i]:
                i+=1
                
            vals.pop ()
                
            helper (vals,i+1)

        helper ([],0)


        return ret

