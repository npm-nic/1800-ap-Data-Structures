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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
        # IF: no root value:
            # create new node
        # IF: value < targeted Node's value --> need to go left 
            # IF: we see that there is no left child,
                # then we can wrap the value in a BSTNode and park it
            # ELSE: there is a child 
                # call the left child's `insert` method 
        # ELSE: value >= Node's value --> need to go right 
            # IF: we see there is no right child, 
                # then we can wrap the value in a BSTNode and park it 
            # ELSE: there is a child 
                # call the right child's `insert` method 
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
        # IF: root value is the target
            # return true
        # IF: target is bigger than current value
            # IF: the right of the current value is empty
                # return False --> there are no more numbers to check --> number not in the tree
            # ELSE: it is not empty ...
                # call contains() on current right node
        # IF: target is smaller than current value:
            # IF: the next node is empty
                # return False --> there are no more numbers to check --> number not in the tree
            # ELSE: it is not empty...
                # call contains() on current left node
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

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

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

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
