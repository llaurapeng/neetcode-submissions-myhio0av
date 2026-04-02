class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        nums = [-1 * num for num in nums]

        heapq.heapify (nums)
        ret = 0
        while k > 0: 
            val = heapq.heappop (nums)
            ret = val
            k-=1

        return ret*-1


        