class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        nstart = newInterval [0]
        nend = newInterval [1]
        ret = []
        for i , interval in enumerate (intervals):
            start = interval [0]
            end = interval [1]

            if nend < start: 
                print (1)
                ret.append ([nstart,nend])
                return ret + intervals [i:]

            elif nstart > end: 
                ret.append ([start,end])

            else: 
                nstart = min (nstart, start)
                nend = max (nend, end)

        ret.append ([nstart, nend])

        return ret
