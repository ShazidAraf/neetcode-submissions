class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:



        H = {}

        for i in range(len(nums)):

            H[nums[i]] = H.get(nums[i],0)+1

            if  H[nums[i]]>1:
                return True

        return False
        