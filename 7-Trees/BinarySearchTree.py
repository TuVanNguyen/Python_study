"""
Implementation of Binary Search Tree
"""

class Node:
    """
    Nodes that make up the BinarySearchTree
    """
    def __init__(self, key: int):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.parent = None

    def getKey(self):
        return self.key
    
    def getLeftChild(self):
        return self.left_child
    
    def getRightChild(self):
        return self.right_child
    
    def getParent(self):
        return self.parent

    def isRoot(self) -> bool:
        return not self.parent
    
    def isLeftChild(self) -> bool:
        return self.parent and self.parent.getLeftChild() == self
    
    def isRightChild(self) -> bool:
        return self.parent and self.parent.getRightChild == self
    
    def isLeaf(self) -> bool:
        return not (self.left_child or self.right_child)
    
    def setKey(self, key: int):
        self.key = key
    
    def setLeftChild(self, child: 'Node'):
        child.parent = self
        self.left_child = child
    
    def setRightChild(self, child: 'Node'):
        child.parent = self
        self.right_child = child
    
    def findSuccessor(self, parent: 'Node'):
        pass

    def spliceOut(self):
        if self.isLeaf() and self.isLeftChild():
            self.parent.leftChild = None
        elif self.isLeaf() and self.isRightChild():
            self.parent.rightChild = None
        elif self.isLeftChild() and self.left_child:
            self.parent.left_child = self.left_child
        elif self.isLeftChild() and self.right_child:
            self.parent.left_child = self.right_child        
        elif self.isRightChild() and self.right_child:
            self.parent.right_child = self.right_child
        elif self.isRightChild() and self.left_child:
            self.parent.right_child = self.left_child



class BinarySearchTree:
    def __init__(self, root: int = None):
        self.root = Node(root)
        self.size = 0

    def __contains__(self, key):
        if self.get(key):
            return True
        return False

    def __iter__(self):
        return self.root.__iter__()

    def __len__(self):
        return self.size
    
    def __str__(self):
        pass
    
    def setRoot(self, root: int):
        self.root = Node(root)

    def put(self, key: int):
        """
        Puts a new node on the tree with key, satisfying all bst properties.
        Args:
            key (int): key of new node
        Returns:
            None
        """
        if self.root:
            self._put(key, self.root)
            self.size += 1
        else:
            self.root = Node(key)
    
    def _put(self, key: int, currentNode: Node):
        """
        Helper function to add new node as a child to another node already in tree
        Args:
            key (int): key of new node
            currentNode (Node): node to consider for parent of new node
        Returns:
            None
        """
        if key == currentNode.getKey():
            return
        elif key < currentNode.getKey():
            if currentNode.getLeftChild():
                self._put(key, currentNode.getLeftChild())
            else:
                currentNode.setLeftChild(Node(key))
                self.size += 1
        else:
            if currentNode.getRightChild():
                self._put(key, currentNode.getRightChild())
            else:
                currentNode.setRightChild(Node(key))
                self.size += 1

    def get(self, key: int):
        """
        Gets key in tree if it exists
        Args:
            key(int): key to search for in tree
        """
        return self._get(key, self.root)
    
    def _get(self, key: int, currentNode: Node):
        """
        Helper function to fetch node
        Args:
            key (int): key to search for in tree
            currentNode (Node): current node to check key in
        """
        if not currentNode:
            return None
        elif key == currentNode.getKey():
            return currentNode
        elif key < currentNode.getKey():
            return self._get(key, currentNode.getLeftChild())
        else:
            return self._get(key, currentNode.getRightChild())
        
    def delete(self, key: int):
        """
        Deletes node in tree if matching key exists
        """
        delete_node = self.get(key)
        if not delete_node:
            raise KeyError('Error, key not in tree')
        self._del(delete_node)
        self.size -= 1

    def _del(self,delete_node: Node):
        """
        """
        if delete_node.isRoot() and delete_node.isLeaf():
            self.root = None
        elif delete_node.isLeaf() and delete_node.isLeftChild():
            delete_node.getParent().setLeftChild(None)
        elif delete_node.isLeaf() and delete_node.isRightChild():
            delete_node.getParent().setRightChild(None)
        elif delete_node.getLeftChild() and delete_node.getRightChild():
            successor = delete_node.findSuccessor()
            successor.spliceOut()
            delete_node.setKey(successor.getKey())
        else:
            delete_node.spliceOut()




        
    def levelOrderTraversal(self):
        if not self.root:
            return ""
        
        tree_string = f"{self.root.getKey()}\n"
        queue = [self.root]

        while queue:
            level_size = len(queue)
            level_string = ""
            for i in range(level_size):
                current_node = queue.pop(0)
                left_child, right_child = None, None
                if current_node.getLeftChild():
                    left_child = current_node.getLeftChild().getKey()
                    queue.append(current_node.getLeftChild())
                if current_node.getRightChild():
                    right_child = current_node.getRightChild().getKey()
                    queue.append(current_node.getRightChild())
                level_string += f"({left_child},{right_child})"
            tree_string += level_string + "\n"
        return tree_string


if __name__ == "__main__":
    bst = BinarySearchTree(5)
    bst.put(4)
    bst.put(6)
    bst.put(3)
    bst.put(8)
    bst.put(10)
    print(bst.levelOrderTraversal())
