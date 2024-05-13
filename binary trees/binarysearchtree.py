class Node:

    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

    def children(self):
        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    """find the given element in this tree, return the node"""
    def find(self, key):
        # recur down from the root of the tree
        return self.__find_helper(key, self.root)

    """recursive function"""
    def __find_helper(self, key, node):
        if node is None:
            return node
        elif key == node.element:
            return node
        elif key < node.element:
            return self.__find_helper(key, node.left)
        else:
            return self.__find_helper(key, node.right)


    """insert a new element e into this tree"""
    def insert(self, e):
        self.size += 1
        self.__insert_helper(e, self.root)

    """recursive function"""
    def __insert_helper(self, e, node):
        if node is None:
            self.root = Node(e)
        elif e <= node.element:
            if node.left is not None:
                # this node has a left child already
                self.__insert_helper(e, node.left)
            else:
                node.left = Node(e)
        elif e > node.element:
            if node.right is not None:
                self.__insert_helper(e, node.right)
            else:
                node.right = Node(e)

    """delete the specified element from this tree"""
    def delete(self, e):
        self.root = self.__delete_helper(e, self.root)

    """recursive function"""
    def __delete_helper(self, e, node):
        if node is None:
            return None
        if e < node.element:
            node.left = self.__delete_helper(e, node.left)
        elif e > node.element:
            node.right = self.__delete_helper(e, node.right)
        else: # e == node.element
            # node has 0 or 1 child
            if node.left is None:
                grandchild = node.right
                node = None
                return grandchild
            if node.right is None:
                grandchild = node.left
                node = None
                return grandchild
            # node has 2 children
            # find its inorder successor
            successor = self.__find_inorder_successor(node.right)
            # copy the value of its successor
            node.element = successor.element
            # remove its successor from this tree
            node.right = self.__delete_helper(successor.element, node.right)
        self.size -= 1
        return node

    @staticmethod
    def __find_inorder_successor(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    """inorder traversal"""
    def inorder(self):
        visited = list()
        if self.root is not None:
            self.__inorder_helper(self.root, visited)
        return visited

    def __inorder_helper(self, node, visited):
        # left child
        if node.left is not None:
            self.__inorder_helper(node.left, visited)
        # parent
        visited.append(node.element)
        # right child
        if node.right is not None:
            self.__inorder_helper(node.right, visited)

    def __str__(self):
        return str(self.inorder())



