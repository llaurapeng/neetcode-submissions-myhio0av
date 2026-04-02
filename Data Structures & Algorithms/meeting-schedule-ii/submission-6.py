class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals: 
            return 0
        
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda i: i.start)
        
        # Step 2: Initialize a dictionary to track room schedules (not the most optimal approach, but preserving original structure)
        res = {1: [[intervals[0].start, intervals[0].end]]}
        num = 1
        
        for i in intervals[1:]:
            curr_start = i.start
            curr_end = i.end

            found = False

            # Step 3: Check if any room can accommodate the current interval
            for key, values in res.items():
                for room in values:
                    if curr_start >= room[1]:  # If current meeting starts after room is free
                        found = True
                        room[1] = curr_end  # Update room's end time to current meeting's end time
                        break
                if found:
                    break

            # Step 4: If no room was found, create a new room
            if not found:
                num += 1
                res[num] = [[curr_start, curr_end]]

        # Step 5: Return the total number of rooms
        return len(res)




