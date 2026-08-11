class MinStack:

    def __init__(self):
        self.stack = []
        self.minu = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.minu:
            self.minu.append(value)
        else:
            self.minu.append(min(value,self.minu[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minu.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minu[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()