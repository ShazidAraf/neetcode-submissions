from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.H = defaultdict(list)   # key -> [[ts, val], ...], appended in increasing ts order

    def set(self, key, value, timestamp):
        self.H[key].append([timestamp, value])

    def get(self, key, timestamp):
        arr = self.H[key]            # defaultdict → empty list if missing, so no KeyError
        res = ""
        l, r = 0, len(arr) - 1
        while l <= r:                # closed interval [l, r]
            m = l + (r - l) // 2
            if arr[m][0] <= timestamp:
                res = arr[m][1]      # valid candidate — but a later ts might also qualify
                l = m + 1            # so search right for a bigger-but-still-≤ timestamp
            else:
                r = m - 1
        return res
        
