import queue_ll as queue
import stack_ll as stack

# Implements a linked list in both a stack and a queue

# This is a stack using a linked list
print("\n THIS IS A STACK:")
s = stack.Stack()
s.push("first")
s.push("second")
s.push("third")
s.push("fourth")
s.push("fifth")
s.print_stack()
print("\n Pop one...")
s.pop()
s.print_stack()

# This is a queue using a linked list
print("\n THIS IS A QUEUE:")
q = queue.Queue()
q.enqueue("first")
q.enqueue("second")
q.enqueue("third")
q.enqueue("fourth")
q.enqueue("fifth")
q.print_queue()
print("\n Dequeue one...")
q.dequeue()
q.print_queue()
