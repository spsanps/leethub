class MyQueue:

    def __init__(self):
        self.stack_main = []
        self.stack_help = []
        
        
        

    def push(self, x: int) -> None:

        while self.stack_main:
            self.stack_help.append(self.stack_main.pop())
            
        self.stack_help.append(x)
        
        while self.stack_help:
            self.stack_main.append(self.stack_help.pop())
        
        

    def pop(self) -> int:
        if self.stack_main:
            return self.stack_main.pop()
        

    def peek(self) -> int:
        return self.stack_main[-1]
        

    def empty(self) -> bool:
        return len(self.stack_main) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()