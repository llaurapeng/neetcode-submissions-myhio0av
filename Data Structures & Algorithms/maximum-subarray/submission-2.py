class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        best = float('-inf')
        curr = 0
        for i in nums:
            curr+=i
            if curr < 0:
                best = max(best, curr)
                curr = 0
            else:
                best = max(best, curr)
        return best
