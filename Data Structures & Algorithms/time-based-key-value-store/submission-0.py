from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.H = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.H[key].append([timestamp,value])
        
    def get(self, key, timestamp):
        if key not in self.H:
            return ""
        tmp = sorted(self.H[key], reverse=True)   # sorted() returns a list; .sort() returns None
        for ts, val in tmp:
            if ts <= timestamp:
                return val
        return ""
        
        
