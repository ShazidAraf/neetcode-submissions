class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1          # closed interval [l, r]
        while l <= r:                    # <= : the last single element still needs checking
            m = l + (r - l) // 2         # overflow-safe midpoint (good interview signal)
            if nums[m] == target:
                return m                 # found it -> return immediately
            elif nums[m] < target:
                l = m + 1                # m ruled out; target is to the RIGHT
            else:                        # nums[m] > target
                r = m - 1                # m ruled out; target is to the LEFT
        return -1                        # window empty -> not present