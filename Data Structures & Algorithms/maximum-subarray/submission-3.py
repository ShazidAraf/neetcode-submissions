class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cum_sum = nums[0]
        res = nums[0]


        for i in range(1,len(nums)):

            if cum_sum<0:
                cum_sum = 0

            cum_sum += nums[i]

            res = max(res,cum_sum)

        return res






        