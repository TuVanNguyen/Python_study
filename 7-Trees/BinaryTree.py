class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left_child = None
        self.right_child = None
    
    def insertLeft(self,node):
        if self.left_child == None:
            self.left_child = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left_child = self.left_child
            self.left_child = t

    def insertRight(self,node):
        if self.right_child == None:
            self.right_child = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right_child = self.right_child
            self.right_child = t

    def getRightChild(self): 
        return self.right_child

    def getLeftChild(self):
        return self.left_child

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
    def evaluate(self):
        pass

    
    def preOrderTraversal(self):
        print(self.getRootVal())
        if self.getLeftChild():
            self.getLeftChild().preOrderTraversal()
        if self.getRightChild():
            self.getRightChild().preOrderTraversal()

    def inOrderTraversal(self):
        if self.getLeftChild():
            self.getLeftChild().inOrderTraversal()
        print(self.getRootVal())
        if self.getRightChild():
            self.getRightChild().inOrderTraversal()

    def postOrderTraversal(self):
        if self.getLeftChild():
            self.getLeftChild().postOrderTraversal()
        if self.getRightChild():
            self.getRightChild().postOrderTraversal()
        print(self.getRootVal())

    def levelOrderTraversal(self, is_root = True):
        if is_root:
            print(self.getRootVal())
        if self.getLeftChild():
            print(self.getLeftChild().getRootVal())
        if self.getRightChild():
            print(self.getRightChild().getRootVal())
        if self.getLeftChild():
            self.getLeftChild().levelOrderTraversal(is_root=False)
        if self.getRightChild():
            self.getRightChild().levelOrderTraversal(is_root=False)

    
    def __str__(self):
        return self._pretty_print()
    
    
    def _pretty_print(self, prefix="", is_tail=True, result=None):
        """
        Generate a pretty-printed string representation of the tree.
        
        Args:
            prefix (str): The prefix to add before the current node.
            is_tail (bool): Whether this node is a tail node.
            result (list): A list to accumulate the string representation.
            
        Returns:
            str: A string representation of the tree.
        """
        if result is None:
            result = []
        
        # Add current node to result
        result.append(f"{prefix}{'└── ' if is_tail else '├── '}{self.key}")
        
        # Determine the children to process
        children = []
        if self.right_child:
            children.append((self.right_child, False))
        if self.left_child:
            children.append((self.left_child, True))
        
        # Process all but the last child with is_tail=False
        for i, (child, is_last) in enumerate(children[:-1]):
            new_prefix = prefix + ("    " if is_tail else "│   ")
            child._pretty_print(new_prefix, False, result)
        
        # Process the last child with is_tail=True if there are children
        if children:
            child, is_last = children[-1]
            new_prefix = prefix + ("    " if is_tail else "│   ")
            child._pretty_print(new_prefix, True, result)
            
        # Return the result
        if prefix == "":  # If this is the root call
            return "\n".join(result)
        
        return result

if __name__ == "__main__":
    a = BinaryTree("a")
    a.insertLeft("b")
    a.insertRight("c")
    a.insertRight("d")
    a.insertLeft("e")
    a.insertRight("f")
    print(a)
    a.levelOrderTraversal()