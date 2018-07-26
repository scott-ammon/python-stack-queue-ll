import linked_list as ll

class Queue:
  def __init__(self):
    self.store = ll.LinkedList()

  def enqueue(self, element):
    self.store.add(element)
    return self

  def dequeue(self):
    return self.store.delete_head()

  def print_queue(self):
    return self.store.print_list()

  def get(self, n):
    return self.store.get(n)