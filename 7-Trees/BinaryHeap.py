"""
Implementation of Binary Heap

The Binary Heap must maintain the following properties:
* for each parent node p:
    * the left child is 2p
    * the right child is 2p + 1
    * heap order property: the value of p must be less than or equal to each of its childrens' 

"""
class BinHeap:
    def __init__(self):
        self.heapList = []

    def insert(self, item):
        """
        Inserts item at the end of binary heap. Automatically reorders the heap to maintain the heap order property.
        Args:
            item (int): item to insert into heap
        Returns:
            None
        """
        self.heapList.append(item)
        self.percUp(len(self.heapList) - 1)

    def percUp(self, item_pos):
        """
        Reorders heap to maintain the heap order property by moving children nodes up the heap (perculating up) 
        if it's bigger than its parent.
        Typically used after insertion.
        Args: 
            item_pos (int): index in heap of the item we're perculating up
        Returns: None
        """
        while item_pos >= 1:
            parent_pos = item_pos // 2
            if self.heapList[parent_pos] > self.heapList[item_pos]:
                temp = self.heapList[item_pos]
                self.heapList[item_pos] = self.heapList[parent_pos]
                self.heapList[parent_pos] = temp
            item_pos = parent_pos

    def deleteMin(self):
        """
        Deletes the node with the minimum value. Automatically reorders nodes to maintain heap properties.
        Args: None
        Returns: 
            min_value (int): the minimum value that was in the heap
        """
        min_value = self.heapList[0]
        self.heapList[0] = self.heapList[-1]
        self.heapList.pop()
        self.percDown(0)
        return min_value
    
    def percDown(self, item_pos):
        """
        Reorders heap to maintain heap properties by moving nodes down the heap (percolating down).
        Typically used after removing an item from heap.
        Args:
            item_pos (int): index in heap of item we're percolating down
        Returns:
            None
        """
        while self.minChild(item_pos):
            min_child = self.minChild(item_pos)
            if self.heapList[item_pos] > self.heapList[min_child]:
                temp = self.heapList[item_pos]
                self.heapList[item_pos] = self.heapList[min_child]
                self.heapList[min_child] = temp
            item_pos = min_child
    
    def minChild(self, item_pos):
        """
        For some node, returns the child node with the minimum value (if it exists)
        Args:
            item_pos (int): the index in heap of a node
        Returns:
            (None): iff no child node exists
            min_child: (int) index in heap of child node with minimum value
        """
        left, right = (item_pos * 2), (item_pos * 2 + 1)
        if left >= len(self.heapList):
            return None
        elif right >= len(self.heapList) or self.heapList[left] < self.heapList[right]:
            return left
        else:
            return right
        


    

if __name__ == "__main__":
    my_heap = BinHeap()
    my_heap.insert(5)
    my_heap.insert(3)
    my_heap.insert(1)
    my_heap.insert(6)
    my_heap.deleteMin()
    print(my_heap.heapList)
        
    