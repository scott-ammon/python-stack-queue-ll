import linked_list as ll

class Stack:
  def __init__(self):
    self.store = ll.LinkedList()
  
  def push(self, element):
    self.store.add(element)
    return self

  def pop(self):
    return self.store.delete_at_end()

  def print_stack(self):
    return self.store.print_list()
  
  def get(self, n):
    return self.store.get(n)