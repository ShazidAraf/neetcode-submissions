class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:                 # converge to a single index
            m = l + (r - l) // 2
            if nums[m] > nums[r]:    # min is strictly to the right
                l = m + 1
            else:                    # nums[m] <= nums[r]: min at m or to the left
                r = m                # keep m as a candidate
        return nums[l]               # l == r → the minimum