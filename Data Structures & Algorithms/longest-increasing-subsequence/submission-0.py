class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #dp[i] = length of longest increasing subsequence from starting from index i to the end 
        dp = [1] * len (nums)

        for i in range (len (nums)-1, -1, -1):
            for j in range (i+1, len (nums)):
                if nums[i] < nums [j]:
                    dp [i] = max (dp [i], 1 + dp [j])


        return max (dp)

