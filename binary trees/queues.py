from linkedlist import LinkedList


class LinkedQueue:
    # underlying data structure is a linked list
    def __init__(self):
        self.queue = LinkedList()

    """return the length of this queue"""
    def __len__(self):
        return self.queue.__len__()

    """return True if this queue is empty, False otherwise"""
    def is_empty(self):
        return self.queue.is_empty()

    """return but not remove the first element"""
    def first(self):
        return self.queue.first()

    """add e to the end of this queue"""
    def enqueue(self, e):
        self.queue.add_last(e)

    """remove and return the first element from this queue"""
    def dequeue(self):
        return self.queue.remove_first()

    """return a string representation of this queue"""
    def __str__(self):
        return self.queue.__str__()


class ListQueue:

    # underlying data structure is a list
    def __init__(self):
        self.queue = list()

    """return the length of this queue"""
    def __len__(self):
        return len(self.queue)

    """return True if this queue is empty, False otherwise"""
    def is_empty(self):
        return len(self.queue) == 0

    """return but not remove the first element"""
    def first(self):
        if self.is_empty():
            return None
        return self.queue[0]

    """add e to the end of this queue"""
    def enqueue(self, e):
        self.queue.append(e)

    """remove and return the first element from this queue"""
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    """return a string representation of this queue"""
    def __str__(self):
        return "(" + str(self.queue).lstrip("[").rstrip("]") + ")"




