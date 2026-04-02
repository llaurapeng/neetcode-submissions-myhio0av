class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort (key = lambda interval: interval [1])
        leng = len (intervals)
        ret = [intervals [0]]
        lengret = 0

        for x in intervals[1:]: 

            start = x [0]
            end = x [1]

            start2 = ret [-1][0]
            end2 = ret [-1][1]

            if start >= end2: 
                #add to the end
                ret.append ([start, end])
            else: 
                lengret+=1

        print (ret)
        return lengret


