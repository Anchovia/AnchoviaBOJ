class Stack:
    def __init__(self):
        self.item = []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()
    
    def peek(self):
        return self.item[-1]
    
    def isEmpty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

    def print(self):
        print(self.item)

# TEST
myStack = Stack()

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.pop()
myStack.push(4)
myStack.push(5)
myStack.pop()
myStack.push(6)
myStack.pop()

print(myStack.peek())
print(myStack.size())
print(myStack.isEmpty())

myStack.print()