# Definition of Stack Class

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        return self.items.pop()
    
    def peek(self):
        """
        Check the top of the stack before popping it
        """
        return self.items[-1]
    
    def __len__(self):
        return len(self.items)

if __name__ == "__main__":
    a = Stack()
    a.push(5)
    a.push(4)
    print(len(a))

    