class Node:

    def __init__(self, element=None):
        self.element = element
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.header = Node()
        self.trailer = Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    # return the length of this list
    def __len__(self):
        return self.size

    # return a boolean to indicate whether the list is empty
    def is_empty(self):
        return self.size == 0

    # return the first element
    def first(self):
        return self.head.next.element

    def last(self):
        return self.trailer.prev.element

    # utility method
    # insert an element e between two nodes p and s
    def __add_between(self, e, p, s):
        # create a new node with e
        newest = Node(e)
        # link p and newest
        p.next = newest
        newest.prev = p
        # link s and newest
        newest.next = s
        s.prev = newest
        # update size
        self.size += 1

    # add a new element to the front of the list
    def add_first(self, e):
        self.__add_between(e, self.header, self.header.next)

    # add a new element e to the end of the list
    def add_last(self, e):
        self.__add_between(e, self.trailer.prev, self.trailer)

    # utility method
    def __remove_node(self, n):
        # find the previous node and next node of n
        p = n.prev
        s = n.next
        # link p and s together
        p.next = s
        s.prev = p
        # remove n from the list
        n.next = None
        n.prev = None
        # update size
        self.size -= 1
        # return the removed element
        return n.element

    # remove the first element and then return it
    def remove_first(self):
        if self.is_empty():
            return None
        return self.__remove_node(self.header.next)

    # remove the last element and then return it
    def remove_last(self):
        if self.is_empty():
            return None
        return self.__remove_node(self.trailer.prev)

    # return a string representation of the list
    def __str__(self):
        ans = "("
        walk = self.header.next
        while walk is not self.trailer:
            ans += str(walk.element) + ", "
            walk = walk.next
        return ans.rstrip(", ") + ")"

