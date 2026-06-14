class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:                     # converge until ONE candidate remains
            m = l + (r - l) // 2
            if nums[m] > nums[r]:        # dip (min) is strictly to the RIGHT of m
                l = m + 1                # m cannot be the min -> eliminate it
            else:                        # nums[m] <= nums[r]
                r = m                    # m MIGHT be the min -> keep it as candidate
        return nums[l]                   # l == r -> the minimum