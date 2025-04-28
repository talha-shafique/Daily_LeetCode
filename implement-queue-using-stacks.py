class MyQueue:

    def __init__(self):
        self.S1=[]
        self.S2=[]
        

    def push(self, x: int) -> None:
        self.S1.append(x)
        
    def pop(self) -> int:
        while self.S1:
            x=self.S1.pop()
            if self.S1:
                self.S2.append(x)
            else:
                break
        while self.S2:
            y=self.S2.pop()
            self.S1.append(y)
        return x

    def peek(self) -> int:
        while self.S1:
            x=self.S1.pop()
            self.S2.append(x)
        while self.S2:
            y=self.S2.pop()
            self.S1.append(y)
        return x
        
    def empty(self) -> bool:
        if self.S1:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()