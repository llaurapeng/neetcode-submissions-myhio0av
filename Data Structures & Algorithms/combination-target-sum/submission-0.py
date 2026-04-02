class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        
        def helper(i, comb, summ): 
            if summ == target:  # We found a valid combination
                ret.append(comb[:])  # Append a copy of comb
                return 
            if summ > target:  # We exceeded the target, no point continuing
                return 
            if i >= len(nums):  # We've exhausted all elements
                return 

            # Include nums[i] and stay at the same index i (allowing repetitions)
            comb.append(nums[i])
            helper(i, comb, summ + nums[i])  # Call with the updated sum

            # Exclude nums[i] and move to the next index
            comb.pop()
            helper(i + 1, comb, summ)  # Call with the next index

        helper(0, [], 0)  # Start with an empty combination and sum = 0
        return ret
