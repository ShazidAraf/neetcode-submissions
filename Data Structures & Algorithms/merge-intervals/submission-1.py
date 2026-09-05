class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort(key=lambda x: x[0]) 
        result = []
        merge_cand = None
        for i in range(len(intervals)):

            if merge_cand is None:
                merge_cand = intervals[i]

            if i<len(intervals)-1:
                y = intervals[i+1]
            else:
                y = intervals[i]


            if merge_cand[1]< y[0]:
                result.append(merge_cand)
                merge_cand = None
            else:
                merge_cand = [min(merge_cand[0],y[0]),max(merge_cand[1],y[1])]

        result.append(merge_cand)

        return result




        