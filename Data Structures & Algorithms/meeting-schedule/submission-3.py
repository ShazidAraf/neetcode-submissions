"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:


        intervals.sort(key = lambda x : x.start)

        # print(intervals)


        for i in range(1,len(intervals)):

            x = intervals[i-1]
            y = intervals[i]

            if x.end>y.start:
                return False


        return True

