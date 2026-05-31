from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:



        H = {}

        for i in nums:
            H[i] = H.get(i,0)+1

        # print(H)

        G = defaultdict(list)

        for i in H.keys():
            G[H[i]].append(i)
        
        # print(G)
        
        G_keys = list(G.keys())
        G_keys.sort()

        # print(G_keys)
        
        result = []

        for i in G_keys[::-1]:

            result+=G[i]

            if len(result)>=k:
                break

        return result


