class MedianFinder:

    def __init__(self):

        self.array_min = []
        self.array_max = []
        

    def addNum(self, num: int) -> None:

        heapq.heappush(self.array_min,-num)


        if self.array_min and self.array_max:

            num1 = - self.array_min[0]
            num2 = self.array_max[0]

            if num1>num2:

                x = - heapq.heappop(self.array_min)
                heapq.heappush(self.array_max,x)


        if len(self.array_min) > len(self.array_max) + 1:

            x = - heapq.heappop(self.array_min)
            heapq.heappush(self.array_max,x)                


        elif len(self.array_max) > len(self.array_min) + 1:

            x = heapq.heappop(self.array_max)
            heapq.heappush(self.array_min,-x)              


    def findMedian(self) -> float:

        # print(self.array_min)
        # print(self.array_max)


        if len(self.array_max) == len(self.array_min):
            return  (-self.array_min[0]+self.array_max[0])/2
        elif len(self.array_max) > len(self.array_min):
            return self.array_max[0]
        elif len(self.array_max) < len(self.array_min):
            return -self.array_min[0]        





        