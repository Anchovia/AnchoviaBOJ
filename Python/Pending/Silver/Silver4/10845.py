import sys

def singleIntInput():
    n = int(sys.stdin.readline().rstrip())

    return n

def queueDataInput():
    rawData = sys.stdin.readline().rstrip()

    if(' ' in rawData):
        idx = rawData.index(' ')

        cmd = rawData[:idx]
        data = rawData[idx + 1:]
    
    else:
        cmd = rawData
        data = 0

    return cmd, int(data)

def push(queue, x):
    queue.append(x)

    return queue

def pop(queue):
    if(len(queue) == 0):
        print(-1)
    
    else:
        print(queue[0])
        del queue[0]

    return queue

def size(queue):
    print(len(queue))

def empty(queue):
    if(len(queue) == 0):
        print(1)
    
    else:
        print(0)

def front(queue):
    if(len(queue) == 0):
        print(-1)
    
    else:
        print(queue[0])

def back(queue):
    if(len(queue) == 0):
        print(-1)
    
    else:
        print(queue[len(queue) - 1])

def judgeCmd(queue, cmd, data):
    if(cmd == 'push'):
        push(queue, data)
    
    elif(cmd == 'pop'):
        pop(queue)
    
    elif(cmd == 'size'):
        size(queue)
    
    elif(cmd == 'empty'):
        empty(queue)
    
    elif(cmd == 'front'):
        front(queue)
    
    elif(cmd == 'back'):
        back(queue)
    
    return queue

def main():
    queue = []

    run = singleIntInput()

    for i in range(0, run):
        cmd, data = queueDataInput()

        queue = judgeCmd(queue, cmd, data)

# __main__
main()