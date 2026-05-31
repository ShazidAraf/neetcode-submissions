class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        result_pre = [1]*len(nums)
        result_post = [1]*len(nums)

        for i in range(len(nums)):

            if i==0:
                result_pre[i] = 1
                continue

            result_pre[i] = result_pre[i-1]*nums[i-1]

        for i in range(len(nums)-1,-1,-1):

            if i==len(nums)-1:
                result_post[i] = 1
                continue
                

            result_post[i] = result_post[i+1]*nums[i+1]

        result = [result_pre[i]*result_post[i] for i in range(len(result_post))]

        return result

