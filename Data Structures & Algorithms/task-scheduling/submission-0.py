from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        H = Counter(tasks)


        maxHeap = [-c for c in H.values()]
        heapq.heapify(maxHeap)

        # print(haxHeap)

        q = deque()
        time = 0

        while maxHeap or q:

            time+=1

            if maxHeap:

                cnt = heapq.heappop(maxHeap) + 1

                if cnt:
                    q.append([cnt,time+n])

            if q:
                if time==q[0][1]:
                    x = q.popleft()
                    heapq.heappush(maxHeap,x[0])

        return time    
                












        
        