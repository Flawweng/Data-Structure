class Stack:

    def __init__(self):
        self.size=0
        self.top=None

    def push(self, value):
        if self.top == None:
            self.top = self.Node(value)
        else:
            self.top = self.Node(value, self.top)
        return self
    
    def __str__(self):
        if self.top == None:
            return "| |"
        else:
            currentNode = self.top
            s = ""
            while currentNode != None:
                s += "| " + str(currentNode.value) +" | \n"
                currentNode = currentNode.next
            return s

    class Node:
        def __init__(self, value, nextNode=None):
            self.value = value
            self.next = nextNode


s = Stack()
s.push("LOL").push("World").push("Hello")
print(s)
