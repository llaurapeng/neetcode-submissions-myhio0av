class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #values to the left are smaller than the right

        def solution (l, r):
            middle = (l+r)//2
            middleVal = nums[middle]

            if l > r: 
                return -1

            if middleVal == target: 
                return middle

            if middleVal < target: 
                return solution (middle+1,r)

            else: #if middleVal > target
                return solution (l,middle-1)


        ret = solution (0, len (nums)-1)

        return ret