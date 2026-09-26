class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2==1:
            return False

        target = sum(nums)//2

        self.flag = False


        def dfs(tgt,i):

            if tgt==0:
                self.flag = True
                return
            
            if tgt<0 or i>len(nums)-1 or self.flag == True:
                return

            for j in range(i,len(nums)):

                dfs(tgt-nums[j],j+1)


        dfs(target,0)

        return self.flag