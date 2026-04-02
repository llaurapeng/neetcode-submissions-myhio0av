class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indices = [(val, idx) for idx, val in enumerate(nums)]
        nums_with_indices.sort()  # sort by values

        l, r = 0, len(nums) - 1

        while l < r:
            left_val, left_idx = nums_with_indices[l]
            right_val, right_idx = nums_with_indices[r]
            summ = left_val + right_val

            if summ == target:
                minn = min (left_idx, right_idx)
                maxx = max (left_idx, right_idx)
                return [minn,maxx]
            elif summ < target:
                l += 1
            else:
                r -= 1

        return []