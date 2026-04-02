class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums: 
            if num not in count: 
                count [num] = 0
            count[num]+=1

        heapp = [[-1 * counter, item] for item, counter in count.items()]
        heapq.heapify (heapp)
        ret = []
        for x in range (k):
            counter, item = heapq.heappop (heapp)
            ret.append (item)

        return ret




        