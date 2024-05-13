from linkedlist import LinkedList

class LinkedStack:

    # underlying data structure is a linked list
    def __init__(self):
        # give a linked list to represent this stack
        self.stack = LinkedList()

    """return the length of this stack"""
    def __len__(self):
        return self.stack.__len__()

    """return True if the stack is empty, False otherwise"""
    def is_empty(self):
        return self.stack.is_empty()

    """return but not remove the top element"""
    def top(self):
        return self.stack.first()

    """add e to the top of this stack"""
    def push(self, e):
        self.stack.add_first(e)

    """remove and return the top element from this stack"""
    def pop(self):
        return self.stack.remove_first()

    """return a string representation of this stack"""
    def __str__(self):
        return self.stack.__str__()



class ListStack:

    # underlying data structure is a list
    def __init__(self):
        self.stack = list()

    """return the length of this stack"""
    def __len__(self):
        return len(self.stack)

    """return True if the stack is empty, False otherwise"""
    def is_empty(self):
        return len(self.stack) == 0

    """return but not remove the top element"""
    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    """add e to the top of this stack"""
    def push(self, e):
        self.stack.append(e)

    """remove and return the top element from this stack"""
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    """return a string representation of this stack"""
    def __str__(self):
        #"""ans = "("
        #for i in range(len(self.stack)-1, -1, -1):
        #    ans += str(self.stack[i]) + ", "
        #return ans.rstrip(", ") + ")""""
        copy = self.stack + []
        copy.reverse()
        return "(" + str(copy).lstrip("[").rstrip("]") + ")"

