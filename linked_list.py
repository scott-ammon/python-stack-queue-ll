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

  # deletes specifc element that matches provided data
  def delete(self, data):
    if (self.head == None):
      return False
    current = self.head
    if(current.data == data):
      # need to delete the head node
      temp_node = current.next_node
      current.next_node = None
      self.head = temp_node
    else:
      # need to keep looping to find the data
      while (current.next_node != None):
        previous = current
        current = current.next_node
        if (current.data == data):
          temp_node = current.next_node
          previous.next_node = temp_node
          current.next_node = None
          return True
      return False

  # insert element before index n, with provided data
  def insert_before(self, n, data):
    node = Node(data)
    if(n == 0):
      # insert before the head
      temp_node = self.head
      self.head = node
      self.head.next_node = temp_node
    else:
      current = self.head
      previous = None
      for i in range(0, n):
        previous = current
        current = current.next_node
        if (current == None):
          previous.next_node = node
          return True
      temp_node = previous.next_node
      previous.next_node = node
      node.next_node = temp_node

  def get(self, n):
    if(self.head):
      if (n == 0):
        return self.head.data
      else:
        current = self.head.next_node
        i = 1
        while(current.next_node != None and i < n):
          current = current.next_node
          i += 1
        if (i == n):
          return current.data
        else:
          return None
    else:
      # empty list
      return None

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