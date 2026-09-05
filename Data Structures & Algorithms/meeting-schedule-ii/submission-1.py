"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:


        start_int = []
        end_int = []

        for i in range(len(intervals)):
            start_int.append(intervals[i].start)
            end_int.append(intervals[i].end)


        start_int.sort()
        end_int.sort()


        i = 0
        j = 0
        count = 0
        res = 0

        while i<len(start_int):

            if start_int[i]<end_int[j]:
                count += 1
                i += 1

            else:
                count -= 1
                j += 1

            res = max(res,count)

        return res

            
            









        