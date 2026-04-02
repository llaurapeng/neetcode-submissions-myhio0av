class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        l, r = max(weights), sum(weights)
        
        while l <= r:
            mid = (l + r) // 2
            currDays = 1
            currSum = 0
            
            for weight in weights:
                if currSum + weight > mid:
                    currDays += 1
                    currSum = 0
                currSum += weight

            if currDays > days:
                l = mid + 1
            else:
                r = mid - 1
        
        return l