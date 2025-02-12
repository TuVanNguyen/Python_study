"""
Full implementation of a queue
"""

class Queue:
    def init(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
    def __len__(self):
        return len(self.items)