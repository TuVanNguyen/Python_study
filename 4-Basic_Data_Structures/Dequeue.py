"""
Implementation of a Dequeue
"""

class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def addFront(self,item):
        self.items.insert(0,item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop()
    
    def __len__(self):
        return len(self.items)