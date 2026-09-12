from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand)%groupSize!=0:
            return False

        H = Counter(hand)
        heap = list(H.keys())
        heapq.heapify(heap)

        while heap:

            min_val = heap[0]
            

            for i in range(min_val,min_val+groupSize):

                if H.get(i,0)==0:
                    return False
                H[i] = H[i] - 1

                if H[i]==0:
                    if i!=heap[0]:
                        return False
                    heapq.heappop(heap)
                    

        return True
        