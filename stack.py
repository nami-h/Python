class Stack(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,x):
        return self.items.append(x)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
s=Stack()
print(s.isEmpty())
print(s.push(3))
print(s.push(True))
print(s.push('BHB'))
print(s.pop())
print(s.peek())
print(s.size())
