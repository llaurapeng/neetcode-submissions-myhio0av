class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid  # Found the target
            
            # Determine which half is sorted
            if nums[l] <= nums[mid]:  # Left half is sorted
                if nums[l] <= target < nums[mid]:  # Target is in the left half
                    r = mid - 1
                else:  # Target is in the right half
                    l = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[r]:  # Target is in the right half
                    l = mid + 1
                else:  # Target is in the left half
                    r = mid - 1
        
        return -1  # Target not found


        