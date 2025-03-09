from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # If there are no meetings, no conference rooms are required.
        if not intervals:
            return 0

        # Extract and sort all start times and end times separately
        start = sorted([i.start for i in intervals])  # Sorted list of meeting start times
        end = sorted([i.end for i in intervals])  # Sorted list of meeting end times

        res = 0  # Maximum number of meeting rooms required
        count = 0  # Ongoing meetings at any given time
        s, e = 0, 0  # Two pointers for traversing start and end times

        # Traverse through all the meeting start times
        while s < len(intervals):
            if start[s] < end[e]:  
                # A new meeting is starting before the previous one ends, so we need a new room
                count += 1  # Increase active meetings
                s += 1  # Move to the next start time
            else:  
                # A meeting has ended, so a room is freed up
                count -= 1  # Decrease active meetings
                e += 1  # Move to the next end time
            
            # Update the maximum number of rooms required
            res = max(res, count)

        return res  # Return the maximum number of rooms required at any time
