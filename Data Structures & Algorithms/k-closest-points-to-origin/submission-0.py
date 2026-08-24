import math

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        point_length = []
        for i in range(len(points)):
            point_length.append([math.sqrt(points[i][0]**2 + points[i][1]**2),points[i]])
    
        heapq.heapify(point_length)

        result = []
        for i in range(k):
            x = heapq.heappop(point_length)
            result.append(x[1])
        
        return result