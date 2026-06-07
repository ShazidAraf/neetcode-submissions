class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        l = 0
        r = len(numbers) - 1

        while l<r:

            if numbers[l] + numbers[r]==target:
                return [l+1,r+1]

            elif numbers[l] + numbers[r]>target:
                r = r-1
            
            elif numbers[l] + numbers[r]<target:
                l = l+1

        

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         n = len(numbers)
#         d = {}
#         for i in range(n):
#             number = numbers[i]
#             if target - number in d:
#                 return [d[target - number] + 1, i + 1]
#             d[number] = i