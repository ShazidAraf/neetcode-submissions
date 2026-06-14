import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)          # speed range: 1 .. biggest pile
        result = r                    # max(piles) always works in <= len(piles) hours

        while l <= r:
            m = l + (r - l) // 2
            hours = sum(math.ceil(p/m) for p in piles)   # integer ceil

            if hours <= h:            # fast enough → try slower, save this
                result = m
                r = m - 1
            else:                     # too slow → must go faster
                l = m + 1
        return result