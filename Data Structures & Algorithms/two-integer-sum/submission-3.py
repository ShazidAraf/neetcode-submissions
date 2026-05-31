from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        H = {}

        for i in range(len(nums)):


            y = target - nums[i]

            if y in H:
                return [H[y],i]
            else:
                # print(H)
                H[nums[i]] = i