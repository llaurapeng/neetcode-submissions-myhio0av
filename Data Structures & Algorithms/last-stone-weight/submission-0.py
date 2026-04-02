class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-1 * stone for stone in stones]
        heapq.heapify (stones)

        while len (stones) > 1: 
            heavystone = heapq.heappop (stones)
            lightstone = heapq.heappop (stones)

            if heavystone != lightstone: 
                newweight = heavystone - lightstone
                heapq.heappush (stones, newweight)

        return stones [0] * -1 if stones else 0
