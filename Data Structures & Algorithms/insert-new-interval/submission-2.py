class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        newStart = newInterval [0]
        newEnd = newInterval [1]
        ret = []
        for i, interval  in enumerate (intervals): 
            start = intervals [i][0]
            end = intervals [i][1]

            if newEnd < start: 
                ret.append ([newStart, newEnd])
                ret.extend (intervals [i:])
                return ret
            #no overlap move onto the next
            elif newStart > end: 
                ret.append ([start,end])
            #there is a overlap
            elif newStart >= start or newEnd >= start and newEnd<= end:
                print ('this')
                newStart = min (start, newStart)
                newEnd = max (end, newEnd)

        ret.append ([newStart, newEnd])

        return ret
                


