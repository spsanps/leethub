
class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        new_min = min(self.stack[-1][1], val) if self.stack else val
        self.stack.append((val, new_min))
        

    def pop(self):
        return self.stack.pop()[0]
        

    def top(self):
        return self.stack[-1][0]
        

    def getMin(self):
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()