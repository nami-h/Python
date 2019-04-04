class Q(object):
  def __init__(self):
    self.items=[]

  def isEmpty(self):
    return self.items==[]

  def enqueue(self, items):
    self.items.insert(0, items)

  def dequeue(self):
    self.items.pop()

  def size(self):
    return len(self.items)

q=Q()
print(q.size())
print(q.isEmpty())
print(q.enqueue(9))
print(q.enqueue(True))
print(q.enqueue("bubu"))
print(q.dequeue())
print(q.isEmpty())
print(q.size())
