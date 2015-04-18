class LinkedList():
  def __init__(self, head=None):
    self.head = head

  def __iter__(self):
    self.current = self.head
    return self

  def __next__(self):
    if not self.current:
      raise StopIteration

    node = self.current
    self.current = self.current.next_node
    return node
  
  def add(self, data):
    self.head = Node(data, self.head)

  def size(self):
    count = 0

    for i in self:
      count += 1

    return count

  def insert(self, data, index=None):
    if not (index and self.head):
      self.add(data)

    previous_node = self.head
    for i, node in enumerate(self):
      if index is i:
        new_node = Node(data, node)
        previous_node.next_node = new_node
      else:
        previous_node = node

  def delete(self, index):
    if not (index and self.head):
      self.head = self.head.next_node

    previous_node = self.head
    for i, node in enumerate(self):
      if index is i:
        previous_node.next_node = node.next_node
      else:
        previous_node = node

  def reverse(self):
    current = self.head
    last_node = None

    while current:
      current.next_node, last_node, current = last_node, current, current.next_node

    self.head = last_node  

class Node():
  def __init__(self, data, next_node=None):
    self.data = data
    self.next_node = next_node

linked = LinkedList()

for i in range(20):
  linked.add(i)

