class MyQueue:

    def __init__(self):
        self.stack_main = []
        self.stack_help = []
        self.front = []
        
        
        

    def push(self, x: int) -> None:

        
            
        self.stack_main.append(x)

        
        

    def pop(self) -> int:
        self.peek()
        if self.stack_help:
            return self.stack_help.pop()
        

    def peek(self) -> int:
        if self.stack_help:
            return self.stack_help[-1]
        elif self.stack_main:
            while self.stack_main:
                self.stack_help.append(self.stack_main.pop())
            return self.stack_help[-1]
        

    def empty(self) -> bool:
        return len(self.stack_main) == 0 and len(self.stack_help) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()