"""
Implementation of a Linked List
"""

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, new_data):
        self.data = new_data

    def setNext(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        if not self.end:
            self.end = self.head


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    def search(self,item):
        current = self.head

        while current != None:
            if current.getData == item:
                return current
            current = current.getNext()
        return None
    
    def remove(self, item):
        if not self.head:
            return
        elif self.head.getData() == item:
            self.head = self.head.getNext()

        previous = self.head
        current = previous.getNext()
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = previous.getNext()
        
        if found and current == self.end:
            previous.setNext(None)
            self.end = previous
        elif found and current:
            previous.setNext(current.getNext())

    def index(self, item):
        count = 0
        current = self.head

        while current:
            if current.getData() == item:
                return count
            current = current.getNext()
            count += 1

    def append(self, item):
        temp = Node(item)
        self.end.setNext(temp)
        self.end = temp



    def __str__(self):
        list_str = ""
        current = self.head
        while current:
            list_str += str(current.getData()) + " "
            current = current.getNext()
        return list_str
    


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    print(my_list)
    my_list.remove(1)
    print(my_list)
    my_list.append(5)
    print(my_list)