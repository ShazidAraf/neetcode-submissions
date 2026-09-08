class Solution:
    def canJump(self, nums: List[int]) -> bool:
        


        goal = len(nums)-1
        curr_idx = len(nums)-1
        


        while curr_idx>=0:

            if nums[curr_idx]+curr_idx>=goal:
                goal = curr_idx
            curr_idx -= 1


        if goal==0:
            return True
        else:
            return False
