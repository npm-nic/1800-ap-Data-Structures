"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    
    HOW:
        create new_node
        --> if empty list
            --> head & tail = new_node
        --> else: 
            --> new_node.next should point to current_head
            --> current_head's previous should poiont to new_node
            --> reassign head to new_node
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.

    HOW: 
        IF: empty list
        --> return None
        ELIF: single element in list
        --> save current head (to be removed)
        --> head & tail = None
        --> return removed value
        ELSE: general case
        --> save current head (to be removed)
        --> change current head's prev.next to None (replaces with None)
        --> update self.head to the next node
    """
    def remove_from_head(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            removed_value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_value
        else:
            removed_value = self.head
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            return removed_value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.

    HOW: 
        create new_node
        IF: empty list:
        --> head & tail = new_node
        ELSE:
        --> current_tail's next should point to new_node
        --> new_node's previous should point to current_tail
        --> reassign tail to new_node
        increment length by 1
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1


    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.

    HOW: 
        IF: empty list
        --> return None
        ELIF: single element in list
        --> save current tail (to be removed)
        --> head & tail = None
        --> decrement length by 1
        --> return removed value
        ELSE: general case
        --> save current tail value (to be removed)
        --> update self.tail to the prev node
        --> change new current tail next to None (previously pointed to old tail)
        --> decrement length by 1
        --> return removed value
    """
    def remove_from_tail(self):
        if not self.tail:
            return None
        elif self.head == self.tail:
            removed_value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_value
        else:
            removed_value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return removed_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if not self.head:
            return None
        elif self.head == self.tail:
            return None
        elif self.head == node:
            return None
        else:
            DoublyLinkedList.delete(self, node)
            DoublyLinkedList.add_to_head(self, node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if not self.head:
            return None
        elif self.head == self.tail:
            return None
        elif self.tail == node:
            return None
        else:
            DoublyLinkedList.delete(self, node)
            DoublyLinkedList.add_to_tail(self, node.value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.

    HOW:
        IF: empty list
        --> return None
        IF: single element in list
        --> head & tail = None
        ELIF: node is head
        --> reassign self.head to next node
        --> delete()
        ELIF: node is tail
        --> reassign self.tail to prev node
        --> delete()
        ELSE:
        --> delete()
    --> decrement length by 1
    """
    def delete(self, node):
        if not self.head:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head == node:
            DoublyLinkedList.remove_from_head(self)
        elif self.tail == node:
            DoublyLinkedList.remove_from_tail(self)
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    HOW:
        IF: empty list
        --> return None
        ELIF: single element in list
        --> return that value
        ELSE:
        --> assign the head to current position
        --> save as max_value and replace as we find larger numbers
        --> iterate through until we reach the tail
            --> compare values
                --> IF larger
                    --> replace the max with the current
                --> ELSE
                    --> set the next node as the new current node
        --> return max_value
    """
    def get_max(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            return self.head.value
        else:
            current_node = self.head
            max_value = current_node.value
            while current_node is not None:
                if current_node.value > max_value:
                    max_value = current_node.value
                    current_node = current_node.next
                else:
                    current_node = current_node.next
            return max_value