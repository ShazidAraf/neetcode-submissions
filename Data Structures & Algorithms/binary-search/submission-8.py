class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:                # <= so the final single element is checked
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1            # exclude m
            else:                    # nums[m] < target
                l = m + 1            # exclude m
        return -1