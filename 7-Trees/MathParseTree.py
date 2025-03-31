import re
import operator

from BinaryTree import BinaryTree

opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

class ParseTree(BinaryTree):
    " Creates a parse tree from a mathematical expression"

    def __init__(self, expression=None):
        super().__init__(None)
        if expression and expression.isdigit():
            self.setRootVal(int(expression))
        elif expression:
            expression = re.sub(r"\s+", "", expression)
            expression = list(expression)
            self.expression = expression
            self.buildTree()

    def buildTree(self):
        current_tree = ParseTree()
        subtrees = []
        for token in self.expression:
            if token == '(':
                subtrees.append(ParseTree())
            elif token == ')':
                new_tree = subtrees.pop()
                if subtrees and not subtrees[-1].left_child:
                    subtrees[-1].left_child = new_tree
                elif subtrees and not subtrees[-1].right_child:
                    subtrees[-1].right_child = new_tree
                else:
                    current_tree = new_tree
            elif token in opers:
                subtrees[-1].setRootVal(token)
            elif subtrees[-1].getRootVal():
                    subtrees[-1].right_child = ParseTree(token)
            else:
                subtrees[-1].left_child = ParseTree(token)
        self.setRootVal(current_tree.getRootVal())
        self.left_child = current_tree.left_child
        self.right_child = current_tree.right_child


    def evaluate(self):
        leftC = self.getLeftChild()
        rightC = self.getRightChild()

        if leftC and rightC:
            fn = opers.get(self.getRootVal())
            if fn:
                return fn(leftC.evaluate(),rightC.evaluate())
        else:
            return self.getRootVal()





if __name__ == "__main__":
    a = ParseTree("(3+(4*5))")
    print(a)
    print(a.evaluate())
    b = ParseTree("(((7+3)*(5*2))*(8+2))")
    print(b)
    print(b.evaluate())