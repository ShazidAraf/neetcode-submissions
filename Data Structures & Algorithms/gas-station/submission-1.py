class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:



        cumsum = 0
        idx = 0 
        diff_sum = 0

        for i in range(len(gas)):

            diff = gas[i] - cost[i]
            diff_sum += diff

            cumsum += diff

            if cumsum<0:
                cumsum = 0
                idx = (i+1)%len(gas)


        if diff_sum<0:
            return -1
        else:
            return idx










            

            
        