class Node():
  def __init__(self, data):
    self.data = data
    self.next_node = None
  
class LinkedList():
  def __init__(self):
    self.head = None

  # adds new node to the end of list
  def add(self, data):
    node = Node(data)
    if (self.head == None):
      # list is empty
      self.head = node
    else:
      current = self.head
      while(current.next_node != None):
        current = current.next_node
      current.next_node = node

  # deletes node from end of list
  def delete_at_end(self):
    # if list empty, return False
    if (self.head == None):
      return False
    current = self.head
    previous = None
    # loop to get to last node
    while(current.next_node != None):
      previous = current
      current = current.next_node
    # set next node ref to None, removes last element
    if (previous == None):
      # only one list item, delete it by removing reference
      self.head = None
    else:
      # delete last item in the list
      previous.next_node = None
    return True

  # deletes node from start (head) of list
  def delete_head(self):
    # if list empty, return False
    if (self.head == None):
      return False
    current = self.head
    # need to delete the head node
    temp_node = current.next_node
    current.next_node = None
    self.head = temp_node
    return True

  # prints entire list
  def print_list(self):
    print_arr = []
    if(self.head != None):
      current = self.head
      print_arr.append(current.data)
      while(current.next_node != None):
        current = current.next_node
        print_arr.append(current.data)
      print(print_arr)
    else:
      print("Empty...")