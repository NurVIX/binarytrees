class TreeNode:

    def __init__(self, element=None):
        self.parent = None
        self.left = None
        self.right = None
        self.element = element

    def __str__(self):
        return "(" + str(self.element) + ")"

    """return the number of children"""
    def children(self):
        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right

    """return the number of children"""
    def num_children(self):
        count = 0
        if self.left is not None:
            count += 1
        if self.right is not None:
            count += 1
        return count

    """return the sibling of this node"""
    def sibling(self):
        if self.parent is None: # root
            return None
        elif self is self.parent.left:
            return self.parent.right
        elif self is self.parent.right:
            return self.parent.left

    """return true if this node is a leaf"""
    def is_leaf(self):
        return self.num_children() == 0

    """set e as the new element and return the old one"""
    def set(self, e):
        old = self.element
        self.element = e
        return old


class BinaryTree:

    def __init__(self):
        self.root = None
        self.size = 0

    """return the number of nodes"""
    def __len__(self):
        return self.size

    """return true if the tree is empty"""
    def is_empty(self):
        return self.size == 0

    """return the root of the tree"""
    def root(self):
        return self.root

    """return true if the given node is the root"""
    def is_root(self, n):
        return n is self.root

    """return an iterable collection of all the nodes"""
    def nodes(self):
        pass

    """return the depth of a node"""
    def depth(self, n):
        if n is self.root:
            return 0
        else: # recur up
            return self.depth(n.parent) + 1

    """return the height of the tree"""
    def height(self):
        return self.__height_(self.root)

    """recursive function"""
    def __height_(self, n):
        if n.is_leaf():
            return 0
        else: # recur down
            return 1 + max(self.__height_(c) for c in n.children())

    """add e as the root of the tree"""
    def add_root(self, e):
        if self.root is not None:
            raise ValueError("Root exists already")
        self.root = TreeNode(e)
        self.size += 1
        return self.root

    """add e as the left child of n"""
    def add_left(self, n, e):
        if n.left is not None:
            raise ValueError("Left child exists already")
        newNode = TreeNode(e)
        newNode.parent = n
        n.left = newNode
        self.size += 1
        return newNode

    """add e as the right child of n"""
    def add_right(self, n, e):
        if n.right is not None:
            raise ValueError("Right child exists already")
        newNode = TreeNode(e)
        newNode.parent = n
        n.right = newNode
        self.size += 1
        return newNode

    """attach t1 and t2 as subtrees"""
    def attach(self, n, t1, t2):
        if not n.is_leaf():
            raise ValueError("n has two children already")
        if not isinstance(t1, BinaryTree):
            raise TypeError("t1 is not a binary tree")
        if not isinstance(t2, BinaryTree):
            raise TypeError("t2 is not a binary tree")
        self.size += t1.size + t2.size
        if not t1.is_empty():
            t1.root.parent = n
            n.left = t1.root
            t1.root = None
            t1.size = 0
        if not t2.is_empty():
            t2.root.parent = n
            n.right = t2.root
            t2.root = None
            t2.size = 0

    """remove n from this tree"""
    def remove(self, n):
        if n.num_children() == 2:
            raise ValueError("n has two children")
        if n.left is not None:
            child = n.left
        else:
            child = n.right
        if child is not None:
            child.parent = n.parent # grandparent becomes parent
        if n is self.root:
            self.root = child
        else:
            if n is n.parent.left:
                n.parent.left = child
            else:
                n.parent.right = child
        self.size -= 1
        n.parent = None
        return n.element

    # traversal algorithms
    # pre-order: parent -> left -> right
    # post-order: left -> right -> parent
    # in-order: left -> parent -> right
    # breadth-first ->
    def pre_order(self):
        visited = list()
        if not self.is_empty():
            self.__pre_order_(self.root, visited)
        return visited

    def __pre_order_(self, n, visited):
        # append n to visited
        visited.append(n) # parent first
        # for each child of n, recur down
        for child in n.children():
            self.__pre_order_(child, visited)

    def post_order(self):
        visited = list()
        if not self.is_empty():
            self.__post_order_(self.root, visited)
        return visited

    def __post_order_(self, n, visited):
        for child in n.children():
            self.__post_order_(child, visited)
        visited.append(n)

    def in_order(self):
        visited = list()
        if not self.is_empty():
            self.__in_order_(self.root, visited)
        return visited

    def __in_order_(self, n, visited):
        if n.left is not None:
            self.__in_order_(n.left, visited)
        visited.append(n)
        if n.right is not None:
            self.__in_order_(n.right, visited)

    def breadth_first(self):
        # dequeue: pop(0)
        # enqueue: append()
        # add root to queue
        visited = list()
        if not self.is_empty():
            queue = list()
            queue.append(self.root)
            while queue:
                front = queue.pop(0)
                visited.append(front)
                for child in front.children():
                    queue.append(child)
        return visited




