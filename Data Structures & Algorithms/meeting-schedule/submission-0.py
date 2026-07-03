"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import numpy as np

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sorted_inds = np.argsort([i.start for i in intervals])
        print(sorted_inds)

        intervals = [intervals[k] for k in sorted_inds]

        for k in range(0, len(intervals)-1):
            if intervals[k].end > intervals[k+1].start:
                return False

        return True