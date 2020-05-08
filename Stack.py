# Implementation of a Stack

class Stack:
    
    def __init__(self, *args):
        self.storage = []
        for arg in args:
            self.push(arg)

    # Push an element on top of the stack
    def push(self, value):
        self.storage.append(value)
        return self
    
    # Remove element on top of the stack
    def pop(self):
        self.storage.pop()
        return self

    # Get the top element of the stack
    def top(self):
        size = len(self.storage)
        return None if size==0 else self.storage[size -1]

    # Get the last element pf the stack
    def peek(self):
        return self.storage[0]

    # Get the size of the stack
    def size(self):
        return len(self.storage)

    # Indicate if stack is empty
    def empty(self):
        return True if len(self.storage) == 0 else False

    # Test if stacks are equals compared to elements values. 
    def equals(self, obj):
        if not isinstance(obj, Stack) or self.size() != obj.size():
            return False
        for i in range(self.size()):
            if self.storage[i] != obj.storage[i]: return False
        return True
 
    def __str__(self):
        return str(self.storage)
