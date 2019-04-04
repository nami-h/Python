class Deque(object):
  def __init__(self):
    self.items=[]
  def isEmpty(self):
    return self.items==[]
  def addfront(self, items):
    self.items.append(items)
  def addback(self,items):
    self.items.insert(0,items)
  def removefront(self):
    return self.items.pop()
  def removerear(self):
    return self.items.pop(0)
  def size(self):
    return len(self.items)

d=Deque()
print(d.isEmpty())
print(d.addfront(6))
print(d.addfront(True))
print(d.addback(8))
print(d.addback("dede"))
print(d.removefront())
print(d.removerear())
print(d.size())

