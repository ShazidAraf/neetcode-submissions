class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort(key = lambda x : x[0])
        k = 0
        res = [0]*len(queries)
        H = []

        # print(res)

        for q, i in sorted((q, j) for j, q in enumerate(queries)):

            while k<len(intervals) and q >= intervals[k][0]:

                l,r = intervals[k]
                heapq.heappush(H, [r -l+1 , r])
                k+=1


            while H and q>H[0][1]:
                heapq.heappop(H)

            if H:
                res[i] = H[0][0]
            else:
                res[i] = -1


        return res



        