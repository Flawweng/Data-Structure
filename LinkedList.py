# LinkedList implementation

class LinkedList:

    def __init__(self, *args):
        self.head = None
        self.size = 0
        for arg in args:
            self.append(arg)

    # Insert new node at the beginning of the list.
    def push(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1
        return self

    # Append at the end of the list a new node with the value passed.
    def append (self, value):
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

    # Add a node at the index with the value passed.
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

    # Remove from the list the node at the index.
    def removeAtIndex(self, index):
        if(self.size - 1 < index):
            raise ValueError("Cannot remove node at index " + str(index) + " - list size: " + str(self.size))
        if index == 0:
            self.head = self.head.next
        else:
            currentNode = self.head
            # Loop until to be at node before the one to be deleted.
            for i in range(index - 1):
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next if currentNode.next.next else None
        self.size -= 1
        return self

    # Remove from the list all nodes with the value passed.
    def remove(self,value):
        if self.head is None: return None
        currentNode = self.head
        previousNode = None
        while currentNode:
            if currentNode.value == value:
                # List has only one element
                if previousNode is None :
                    self.head = currentNode.next
                else:
                    # Link previous node to next node
                    previousNode.next = currentNode.next
                self.size -= 1
            previousNode = currentNode
            currentNode = currentNode.next
        return self
        
    # Search and return nodes existing in the list with the value passed.
    def search(self, value):
        result = []
        currentNode = self.head
        while currentNode:
            if currentNode.value == value:
                result.append(currentNode)
            currentNode = currentNode.next
        return result
    
    # Reverse the list
    def reverse(self):
        currentNode = self.head
        previousNode = None
        nextNode = None
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        self.head = previousNode
        return self

    # Test if lists are equals compared to elements values. 
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

