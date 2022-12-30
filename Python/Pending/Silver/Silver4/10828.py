import sys

def singleIntegerInput():
    a = int(sys.stdin.readline())

    return a

def dataInput():
    data = sys.stdin.readline().rstrip()

    if(data.find(' ') == -1):
        a = data
        b = 0
    
    else:
        blankIndex = data.find(' ')

        a = data[:blankIndex]
        b = data[blankIndex + 1:]
    
    return a, int(b)

def push(stack, x):
    stack.append(x)

    return stack

def pop(stack):
    if(len(stack) > 0):
        print(stack[len(stack) - 1])
        del stack[len(stack) - 1]
    
    else:
        print(-1)

    return stack

def size(stack):
    print(len(stack))

def empty(stack):
    if(len(stack) == 0):
        print(1)
    
    else:
        print(0)

def top(stack):
    if(len(stack) > 0):
        print(stack[len(stack) - 1])
    
    else:
        print(-1)

def judgeCommend(stack, command, data):
    if(command == 'push'):
        stack = push(stack, data)

    elif(command == 'pop'):
        stack = pop(stack)

    elif(command == 'size'):
        size(stack)

    elif(command == 'empty'):
        empty(stack)

    elif(command == 'top'):
        top(stack)
    
    return stack

def main():
    stack = []

    n = singleIntegerInput()

    for i in range(0, n):
        command, data = dataInput()

        stack = judgeCommend(stack, command, data)

# __main__
main()