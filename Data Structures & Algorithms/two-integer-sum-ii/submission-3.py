class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers is increasing order
        #index needs to LESS than the second number
        #cannot be equal

        for ind, num in enumerate (numbers): 
            remainingNeeded = target - num

            #check in the rest of the array if the value is there
            if ind != len (numbers)-1 and remainingNeeded in numbers [ind+1:]:
                #the remaining in the array 
                #find the index of this number
                return [ind+1, numbers.index (remainingNeeded)+1]
