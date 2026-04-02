class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        vals = {
        }

        for num in nums: 
            if num not in vals: 
                vals [num] = 0

            vals [num]+=1


        index = 0

        for i in range (3):
            if i in vals:
                count = vals [i]
            else: 
                count = 0

            for ind in range (count):
                nums[index] = i
                index+=1

        
    
        