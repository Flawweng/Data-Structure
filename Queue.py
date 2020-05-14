# Queue implementation
class Queue:
    
    def __init__(self,*args):
        self.storage=[]
        for arg in args:
            self.enqueue(arg)
    
    # Adds item to the queue.
    def enqueue(self,item):
        self.storage.append(item)
        return self

    # Removes an item from the queue. The items are popped in the same order in which they are pushed.
    def dequeue(self):
        return None if self.empty() else self.storage.pop(0)

    # Returns if queue is empty.
    def empty(self):
        return len(self.storage) ==0
    
    # Returns the front item from the queue.
    def front(self):
        return None if self.empty() else self.storage[0]

    # Get the last item from the queue.
    def rear(self):
        return None if self.empty() else self.storage[self.size()-1]

    # Get the size of the queue.
    def size(self):
        return len(self.storage)

    # Reverse the stack with recursion.
    def reverse(self):
        if not self.empty():
            front = self.front()
            self.dequeue()
            self.reverse()
            self.enqueue(front)
        return self
   # Sort the queue with recursive way.
    def sort(self):
        if not self.empty():
            front = self.dequeue()
            self.sort()
            self.sortInsert(front)

    # Insert item in sorted stack
    def sortInsert(self,item):
        if self.empty():
            self.enqueue(item)
        # Assume it is sorted from front to rear. Place in front it value is less than front.
        elif self.front() > item: 
            self.storage.insert(0, item) 
        # Forward the item in the queue (after first element) in order to place it at the right place
        else:
            front = self.dequeue()
            self.sortInsert(item)
            self.storage.insert(0, front) 

    # Test if queues are equals, compared to elements values. 
    def equals(self, obj):
        if not isinstance(obj, Queue) or self.size() != obj.size():
            return False
        for i in range(self.size()):
            if self.storage[i] != obj.storage[i]: return False
        return True
    
    def __str__(self):
        return str(self.storage)
            


