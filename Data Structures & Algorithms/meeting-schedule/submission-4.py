"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len (intervals) ==0  : 
            return True

        intervals.sort (key = lambda i:i.start)
        prev = [intervals[0].start, intervals [0].end]

        for obj in intervals[1:]: 
            if prev[1] <= obj.start: 
                prev = [obj.start, obj.end]

            else: 
                return False

        return True

            


