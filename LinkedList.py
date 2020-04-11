class LinkedList:

    def __init__(self, *args):
        self.head = None
        self.size = 0
        for arg in args:
            self.add(arg)

    # Add at the last element of the list, a new node with the value passed as argument.
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

    # Add the element at index
    def addAtIndex(self, value, index):
        # No insert if index superior to 
        if(self.size - 1 < index):
            raise ValueError("Cannot insert node at index " + str(index) + " - list size: " + str(self.size))
        currentNode = self.head
        i = 0
        while i < index -1:
            currentNode = currentNode.next
            i += 1
        currentNode.next = self.Node(value, currentNode.next)
        self.size += 1

    # Remove element at index
    def removeAtIndex(self, index):
        if(self.size - 1 < index):
            raise ValueError("Cannot remove node at index " + str(index) + " - list size: " + str(self.size))
        currentNode = self.head
        if index == 0:
            self.head = currentNode.next
        else:
            i = 0
            while i < index -1:
                currentNode = currentNode.next
                i += 1
            currentNode.next = currentNode.next.next if currentNode.next.next else None
        self.size -= 1


    # Remove from the list all nodes with the value passed as argument
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

    # Return nodes list with the value passed as parameter
    def search(self, value):
        result = []
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value == value:
                result.append(currentNode)
            currentNode = currentNode.next
        return result
                
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

l = LinkedList(1, 2, "LOL", "Yes", 2)
l.removeAtIndex(2)
print("Remove element at index 2: " + str(l) + " - Size: " + str(l.size))

