class MinStack():

    def __init__(self):                        #constructor type for initializing the sttributes of the class 
        self.items=[]
        
    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[len(self.items)-1]

    def getMin(self) -> int:
        return min(self.items)


# Your MinStack object will be instantiated and called as such:
#obj = MinStack()
#obj.push(x)
#obj.pop()
#param_3 = obj.top()
#param_4 = obj.getMin()
