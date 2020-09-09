class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
  def get_value(self):
    return self.value
  def get_next_node(self):
    return self.next_node
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  # ----------> add_to_tail <---------- [1]
  def add_to_tail(self, value):
    new_node = Node(value)
    if not self.tail: 
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next_node(new_node)
      self.tail = new_node
    self.length += 1
  # ----------> remove_head <---------- [2]
  def remove_head(self):
    if not self.head:
      return None
    if self.head is self.tail:
      head = self.head
      self.head = None
      self.tail = None
      self.length -= 1
      return head.get_value()
    else:
      value = self.head.get_value()
      self.head = self.head.get_next_node()
      self.length -= 1
      return value
  # ----------> remove_tail <---------- [3]
  def remove_tail(self):
    if not self.tail:
      return None
    if self.head is self.tail:
      value = self.head.get_value()
      self.head = None
      self.tail = None
      self.length -= 1
      return value
    else:
      current = self.head
      while current.get_next_node() is not self.tail:
        current = current.get_next_node()
      value = self.tail.get_value()
      self.tail = current
      self.length -= 1
      return value

''' 
[1] add_to_tail
create a new node
--> IF: no tail (empty list)
    --> set self.head and self.tail to new_node
--> ELSE: a tail (general case)
    --> set current last node's next reference to the new_node -- self.tail.set_next_node(new_node)
    --> set 'new' last node (self.tail) to point to new_node
--> increment self.length by 1

[2] remove_head
--> IF: no head (empty list)
    --> return None
--> IF: head is tail (list has only one element): 
    --> set self.head to current_head.next (which is None)
    --> set self.tail to None
    --> decrement self.length by 1
--> ELSE: a head & list > 1 element (general case)
    --> set self.head to current_head.next
    --> return current_head.value
    --> decrement self.length by 1

[3] remove_tail
--> IF: no tail (empty list)
    --> return None
--> IF: head is tail (list has only one element): 
    --> save current_tail.value
    --> set self.tail to None
    --> set self.head to None
--> ELSE (general case):
    --> iterate thru list and end at next-to-last node
        --> save current_tail (next-to-last) value
    --> set tail to current_node
    --> set current_node.next to None
'''











    # def contains(self, value):
    #     if not self.head:
    #         return False

    #     # get a reference to the node we're currently at; update this as we traverse the list
    #     current = self.head

    #     while current:
    #         # return true if the current value we're looking at matches our target value
    #         if current.get_value() == value:
    #             return True
    #         # update our current node to the current's node next node
    #         current = current.get_next_node()
    #     # if we've gotten here, then the target node isn't in our list
    #     return False

    # def get_max(self):
    #     if not self.head:
    #         return None
    #     # reference to the largest value we've seen so far
    #     max_value = self.head.get_value()
    #     # reference to our current node as we traverse the list
    #     current = self.head.get_next_node()
    #     # check to see if we're still at a valid list node
    #     while current:
    #         # check to see if the current value is greater than the max_value
    #         if current.get_value() > max_value:
    #             # if so, update our max_value variable
    #             max_value = current.get_value()
    #         # update the current node to the next node in the list
    #         current = current.get_next_node()
    #     return max_value