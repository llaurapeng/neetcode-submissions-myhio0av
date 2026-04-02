class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #l pointer is where ou can subsitite a new unique value
        #r pointer is try to find a new unique value
        l, r = 0, 1

        while r < len (nums):
            if nums [l] != nums [r]:
                nums [l+1] = nums [r]
                l+=1
            r+=1

        return l+1
        

            

