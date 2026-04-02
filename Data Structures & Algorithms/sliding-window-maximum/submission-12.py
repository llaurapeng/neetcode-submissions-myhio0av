class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        heap = []
        ret = []
        #apply reverse for each value in nums

        nums = [-1 * num for num in nums]

        for i in range (len (nums)):
            if i == l+k-1:
                #at then end
                section = nums [l:i+1]
                heapq.heapify (section)
                ret.append (heapq.heappop (section)* -1)
                l+=1

        return ret






            
