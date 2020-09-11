"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # ---------> insert() <---------
        # IF: no root value:
            # create new node
        # IF: target < node.value --> go left
            # IF: node.left is None
                # create node here
            # ELSE:
                # do the same thing --> insert target into node.left
        # ElSE: value >= Node's value --> go right 
            # IF: node.right is None
                # create node here
            # ELSE: there is a node.right
                # do the same thing --> insert target into node.right
    def insert(self, value):
        if self is None:
            self = BSTNode(value)
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    # --------> contains() <----------
        # IF: root value is the target
            # return true
        # IF: target > current value --> go right
            # IF: node.right is empty
                # --> there are no more numbers to check <--> number not in the tree
                # RETURN false
            # ELSE: node.right is not empty ...
                # RETURN contains() on node.right
        # IF: target < current value --> go left
            # IF: node.left is empty
                # --> there are no more numbers to check --> number not in the tree
                # RETURN false 
            # ELSE: node.left is not empty...
                # RETURN call contains() on node.left 
    def contains(self, target):
        if self.value ==  target:  
            return True
        if target > self.value:
            if self.right is None:
                return False
            else: 
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
    

    # Return the maximum value found in the tree
    # --------> get_max() <---------
        # IF: the next right node is empty --> biggest node is the root
            # return that value 
        # ELSE: there is another (larger) number to the right...
            # return a recursion to check the next node
            # AKA: Call the get_max function on the node to the right
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node
    # --------> for_each <---------
        # call the anonymous function on self.value
        # IF: this node has a right child
            # pass the anonymous function to it
        # IF: this node has a left child
            # pass the anonymous function to it
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)





    # ----- Part 2 (Day 4) -----

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # ----------> in_order_print() <----------
        # IF: theres a smaller number (aka self.left exists)
            # run again on that node
        # PRINT: once you are all the way left
        # IF: theres a node to the right
            # run again on that node
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # ----------> bft_print() <----------
    def bft_print(self):
        queue = Queue()
        if self is None:
            return
        current = self
        queue.enqueue(current)
        while (len(queue) > 0):
            current = queue.dequeue()
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # ----------> dtf_print() <----------
    def dft_print(self):
        stack = Stack()
        if self is None:
            return
        current_node = self
        stack.push(current_node)
        while len(stack):
            current_node = stack.pop()
            print(current_node.value)

            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

print('--- in_order_print ---')
bst.in_order_print()
print('--- bft_print ---')
bst.bft_print()
print('--- dft_print ---')
bst.dft_print()

# print("elegant methods")
# # print("pre order")
# # bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
