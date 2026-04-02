class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = math.floor (len (nums) /3)
        ret = []
        count = {}

        for num in nums: 
            if num not in count:
                count [num] = 0

            count [num]+=1
        print (count)
        for num, count in count.items():
            if count > times:
                ret.append (num)

        return ret
        