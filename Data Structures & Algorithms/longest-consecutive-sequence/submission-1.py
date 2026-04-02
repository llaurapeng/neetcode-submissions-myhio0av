class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set (nums)
        longest = 0

        for x in nums: 
            length = 1
            if x-1 not in nums: 
                i = 1
                while x+i in nums: 
                    length+=1
                    i+=1
          
            longest = max (longest, length)

        return longest


