"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [x.start for x in intervals]
        end = [x.end for x in intervals]

        start.sort()
        end.sort()

        startp = 0 
        endp = 0 

        count = 0 
        res = 0

        while startp < len (intervals):

            if start [startp] < end [endp]:
                count+=1
                startp+=1
            
            elif end [endp] <= start [startp]:
                count-=1
                res = max (count, res)
                endp+=1

            res = max (count, res)

        return res