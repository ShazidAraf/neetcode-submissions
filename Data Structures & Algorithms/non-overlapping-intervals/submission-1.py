class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:


        intervals.sort(key = lambda x: x[0])
        print(intervals)
        s_temp,e_temp = intervals[0]
        count = 0

        for i in range(1,len(intervals)):

            s,e = intervals[i]

            if s<e_temp:
                e_temp = min(e_temp,e)
                count = count+1
            else:
                e_temp = e


        return count


        