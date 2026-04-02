class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum (nums) /2
        def dfs (i, summ):

            if summ == target:
                return True

            if i >= len (nums):
                return False


            return dfs (i+1, summ+ nums [i]) or   dfs (i+1, summ)

        return dfs (0, 0)

        