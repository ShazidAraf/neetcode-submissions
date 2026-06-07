class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums.sort()

        results = []


        for i in range(len(nums)):

            if i>0 and nums[i]== nums[i-1]:
                continue

            a = nums[i]

            l = i+1
            r = len(nums)-1


            while l<r:

                s = a+nums[l]+nums[r]

                if s==0:
                    results.append([a,nums[l],nums[r]])
                    
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1

                elif s>0:
                    r = r-1

                elif s<0:
                    l = l+1

            
        return results

