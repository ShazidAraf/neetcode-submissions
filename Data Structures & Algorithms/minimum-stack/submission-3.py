class MinStack:

    def __init__(self):

        self.stack = []
        self.min_ = []
        

    def push(self, val: int) -> None:

        self.stack.append(val)

        if not self.min_:
            self.min_.append(val)
        else:
            tmp = min(self.min_[-1],val)
            self.min_.append(tmp)

    def pop(self) -> None:
        self.stack.pop()
        self.min_.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_[-1]
        
