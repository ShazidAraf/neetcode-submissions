class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        unique_number = set(nums)
        max_length = 0


        for i in range(len(nums)):


            if nums[i]-1 not in unique_number:
                l = 0

                while nums[i]+l in unique_number:
                    l+=1

                max_length = max(max_length,l)

            
        return max_length


        