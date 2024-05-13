class Node:

    # a node has two attributes
    def __init__(self, element=None):
        self.element = element # element stored in this node
        self.next = None # reference to its next node

class LinkedList:

    def __init__(self):
        self.size = 0  # number of elements
        self.head = None  # first node
        self.tail = None  # last node

    """length of the linked list"""
    def __len__(self):
        return self.size

    """return a boolean to indicate whether this 
    linked list is empty or not"""
    def is_empty(self):
        return self.size == 0

    """return the first element (not the first node)"""
    def first(self):
        if self.is_empty():
            return None
        return self.head.element

    """return the last element (not the last node)"""
    def last(self):
        if self.is_empty():
            return None
        return self.tail.element

    """add a new element e to the front of the list"""
    def add_first(self, e):
        # create a node with element e
        newest = Node()
        newest.element = e
        # have this node point at the current head
        newest.next = self.head
        # this new node should become the new head
        self.head = newest
        # special case: linked list was empty before insertion
        if self.size == 0:
            self.tail = self.head
        # update size
        self.size += 1

    """add a new element e to the end of the list"""
    def add_last(self, e):
        # create a new node with element e
        newest = Node(e)
        if self.size == 0:
            self.head = newest
        else:
            # have the current tail point at this new node
            self.tail.next = newest
        # this new node should become the new tail
        self.tail = newest
        # update size
        self.size += 1

    """remove and return the first element"""
    def remove_first(self):
        if self.is_empty():
            return None
        # find the next node of the head
        old_head = self.head
        # the next node should become the new head
        self.head = self.head.next
        # have the old head point at None
        old_head.next = None
        # update size
        self.size -= 1
        # special case: size becomes 0
        if self.size == 0:
            self.tail = None
        # return the element in the old head
        return old_head.element

    """return a string representation of this linked list"""
    def __str__(self):
        ans = "("
        walk = self.head
        while walk is not None:
            ans = ans + str(walk.element) + ", "
            walk = walk.next
        return ans.rstrip(", ") + ")"

    def __iter__(self):
        walk = self.head
        while walk is not None:
            yield walk.element
            walk = walk.next

    def __contains__(self, e):
        walk = self.head
        while walk is not None:
            if walk.element == e:
                return True
            walk = walk.next
        return False



