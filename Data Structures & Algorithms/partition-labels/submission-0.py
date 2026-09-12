class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # H = defaultdict(list)
        H = {}
        # print(H)


        for i in range(len(s)):

            if H.get(s[i],0) == 0:
                H[s[i]] = [i,i]

            else:
                H[s[i]][1] = i

        intervals = list(H.values())
        intervals.sort(key=lambda x: x[0])

        res = []
        start = 0
        end = 0

        for i in range(len(intervals)):
            end = max(end, intervals[i][1])          # running furthest end

            if i == len(intervals)-1 or end < intervals[i+1][0]:
                res.append(end - start + 1)
                start = end + 1

        return res




        