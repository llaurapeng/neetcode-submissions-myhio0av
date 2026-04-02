class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashmap = {0:1}
        summ = 0
        ret = 0

        for num in nums:
            summ+= num

            needed = summ - k

            if needed in hashmap:
                ret+=hashmap[needed] 

            if summ not in hashmap:
                hashmap[summ] = 1

            else:
                hashmap [summ]+=1

        return ret

