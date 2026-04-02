class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals
        
        intervals.sort()  # Sort intervals based on the start value
        ret = [intervals[0]]
        intervals = deque(intervals[1:])  # Initialize deque with remaining intervals
        
        while intervals: 
            val = intervals.popleft()
            start = val [0]
            end = val [1]

            start2 = ret [-1][0]
            end2 = ret[-1][1]
            if start <= end2: 
                print ('overlap')
                ret[-1] = [min (start, start2), max (end, end2)]

            else: 
                #no overlap
                ret.append ([start,end])

        return ret




        







