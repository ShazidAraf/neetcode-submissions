class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        

        def rob_linear(numbers):
            
            prev2, prev1 = 0,0

            for x in numbers:
                prev2, prev1 = prev1, max(prev1 , prev2+x)

            return prev1
        
        c1 = rob_linear(nums[0:-1])
        c2 = rob_linear(nums[1:])
        
        return max(c1,c2)