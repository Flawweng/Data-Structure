class LinkedList:

    def __init__(self, *args):
        self.head = None
        self.size = 0
        for arg in args:
            self.add(arg)

    """
    Add at the end of the list a new node with the value passed.
    """
    def add(self, value):
        # List is empty
        if self.head is None:
            self.head = self.Node(value)
        else:
           # Find the last node and new node
           tail = self.head
           while tail.next != None:
                tail = tail.next
           tail.next = self.Node(value)
        self.size += 1
        return self

    """
    Add a node at the index with the value passed.
    """
    def addAtIndex(self, value, index):
        # No insert if index superior to. 
        if(self.size - 1 < index):
            raise ValueError("Cannot insert node at index " + str(index) + " - list size: " + str(self.size))
        currentNode = self.head
        # Loop until to be at node before the one to added.
        for i in range(index - 1):
            currentNode = currentNode.next
            i += 1
        currentNode.next = self.Node(value, currentNode.next)
        self.size += 1
        return self

   """
   Remove from the list the node at the index.
   """ 
    def removeAtIndex(self, index):
        if(self.size - 1 < index):
            raise ValueError("Cannot remove node at index " + str(index) + " - list size: " + str(self.size))
        if index == 0:
            self.head = self.head.next
        else:
            currentNode = self.head
            # Loop until to be at node before the one to be deleted.
            for i in range(index - 1):
                print(i)
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next if currentNode.next.next else None
        self.size -= 1
        return self


    """
    Remove from the list all nodes with the value passed.
    """ 
    def remove(self,value):
        # Test if list is empty
        if(self.head is not None):
            currentNode = self.head
            previousNode = None
            # Loop on all nodes
            while currentNode is not None:    
                # Test if node has to be remove
                if currentNode.value == value:
                    # First element has to be removed
                    if(previousNode == None):
                        self.head = currentNode.next
                        # List had only one element, list is empty
                        if self.head is None:
                            self.size -= 1
                            return self
                    else:
                        # Remove last element
                        if currentNode.next is None:
                            previousNode.next = None
                            self.size -= 1
                            return self
                        # Remove current element
                        previousNode.next = currentNode.next
                    self.size -= 1
                # Forward on the list
                previousNode = currentNode
                currentNode = currentNode.next
        return self

    """
    Search and return nodes existing in the list with the value passed.
    """ 
    def search(self, value):
        result = []
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value == value:
                result.append(currentNode)
            currentNode = currentNode.next
        return result
    """
    Test if lists are equals compared to elements values. 
    """ 
    def equals(self, obj):
        if not isinstance(obj, LinkedList) or self.size != obj.size:
            return False
        currentNode = self.head
        currentObjNode = obj.head
        for i in range(self.size):
            if currentNode.value != currentObjNode.value: return False
            currentNode = currentNode.next
            currentObjNode = currentObjNode.next
        return True
                
    def __str__(self):
        if self.head is None:
            return "No Element"
        else:
            return self.head.toString()

    class Node:
        def __init__(self, value, nextNode=None):
            self.value = value
            self.next = nextNode

        def toString(self):
            return '{node.value} --> {node.next}'.format(node=self)

        def __str__(self):
            return self.toString()

if __name__ =="__main__":
    l = LinkedList(1, 2, "LOL", "Yes", 2) 
    m = LinkedList(1, 2, "LOL", "Yes", 22)
    print(l.equals(m))




"""
l = LinkedList(1, 2, "LOL", "Yes", 2)
print(str(l) + "- Size: " + str(l.size))
print("Remove element : 1")
l.remove(1)
print(str(l) + " - Size: " + str(l.size))

l = LinkedList(1, 2, "LOL", "Yes", 2)
print("Remove element : 2")
l.remove(2)
print(str(l) + " - Size: " + str(l.size))

l = LinkedList(1, 2, "LOL", "Yes", 2)
print("Remove element : Yes")
l.remove("Yes")
print(str(l) + " - Size: " + str(l.size))

l = LinkedList(1, 2, "LOL", "Yes", 2)
l.search(2)
print("Search for element 2: " + " ".join(str(node) for node in l.search(2)))

l.addAtIndex("Test", 4)
print("Add at index 4 : " + str(l) + " - Size: " + str(l.size))
"""
l = LinkedList(1, 2, "LOL", "Yes", 2)
print(l)
l.removeAtIndex(2)
print("Remove element at index 0: " + str(l) + " - Size: " + str(l.size))
