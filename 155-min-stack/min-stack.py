class MinStack:
    # idea:
    # create 2 stack
    # one holds each elements
    # another one holds min of current stack
    # so when add/push to stack, compare new element vs. currrent min
    # when pop from stack, pop from min_stack as well
    # when getMin, then just check top of min_stack as that should be min of current stack

    # code: O(1) time

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # update val to be min of either val or (top of stack if stack not empty, if empty, take val)
        # val = min(val, self.min_stack[-1] if self.min_stack else val)
        if self.min_stack and self.min_stack[-1] < val:
            val = self.min_stack[-1]
        self.min_stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()