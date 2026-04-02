class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        subset = []
        def helper (dex):

            if dex >= len (nums):
                ret.append (subset.copy())
                return             
            subset.append (nums[dex])
            helper (dex+1)
            subset.pop ()
            helper (dex+1)

        helper (0)
        return ret

