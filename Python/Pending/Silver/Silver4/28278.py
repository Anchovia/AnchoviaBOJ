import sys

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self, x):
        self.stack.append(x)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.stack.pop()
    
    def len(self):
        return self.size
    
    def isEmpty(self):
        if self.size == 0:
            return 1
        else:
            return 0
        
    def top(self):
        if self.size == 0:
            return -1
        else:
            return self.stack[self.size - 1]

def main():
    n = int(input())
    stack = Stack()

    for _ in range(n):
        dataList = list(map(int, sys.stdin.readline().rstrip().split()))
        if dataList[0] == 1:
            stack.push(dataList[1])
        elif dataList[0] == 2:
            print(stack.pop())
        elif dataList[0] == 3:
            print(stack.len())
        elif dataList[0] == 4:
            print(stack.isEmpty())
        else:
            print(stack.top())
main()  