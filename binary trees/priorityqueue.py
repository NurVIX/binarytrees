class PriorityQueue:

    def __init__(self):
        # underlying data structure is a list
        self.heap = list()

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return self.__len__() == 0

    """return the minimum element"""
    def min(self):
        if self.is_empty():
            return None
        return self.heap[0]

    """utility method"""
    @staticmethod
    def __parent(i):
        return (i - 1) // 2

    @staticmethod
    def __left(i):
        return 2 * i + 1

    @staticmethod
    def __right(i):
        return 2 * i + 2

    """return true if it has a left child"""
    def __has_left(self, i):
        return self.__left(i) < len(self.heap)

    """return true if it has a right child"""
    def __has_right(self, i):
        return self.__right(i) < len(self.heap)

    """swap elements at index i and j"""
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    """upheap"""
    def __upheap(self, j):
        parent = self.__parent(j)  # index of j' parent
        if j > 0 and self.heap[j] < self.heap[parent]:
            self.__swap(j, parent)  # swap j and its parent
            self.__upheap(parent)  # recur up from its parent

    def insert(self, e):
        # add e as the last node in heap
        self.heap.append(e)
        # perform upheap to restore the heap order
        self.__upheap(len(self.heap)-1)

    """downheap"""
    def __downheap(self, j):
        if self.__has_left(j):  # if j has a left child
            left = self.__left(j)  # index of j's left child
            smaller_child = left
            if self.__has_right(j):  # if j has a right child
                right = self.__right(j)   # index of j's right child
                if self.heap[right] < self.heap[left]: # right child < left child
                    smaller_child = right  # smaller child is right child
            if self.heap[smaller_child] < self.heap[j]:
                self.__swap(smaller_child, j)
                self.__downheap(smaller_child)  # recur down from j's smaller child

    def remove(self):
        if self.is_empty():
            return None
        self.__swap(0, len(self.heap)-1)
        removed = self.heap.pop()  # remove the last node from heap
        self.__downheap(0)  # restore the heap order from the root
        return removed

    def __str__(self):
        return str(self.heap)




