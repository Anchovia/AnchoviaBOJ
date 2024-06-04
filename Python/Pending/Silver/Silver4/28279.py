from collections import deque
from sys import stdin

def main():
    queue = deque()
    n = int(input())
    queueLen = 0
    for _ in range(n):
        cmd, x = 0, 0
        dataInput = stdin.readline().rstrip()
        if ' ' in dataInput:
            cmd, x = map(int, dataInput.split())
        else:
            cmd = int(dataInput)
        if cmd == 1:
            queue.appendleft(x)
            queueLen += 1
        elif cmd == 2:
            queue.append(x)
            queueLen += 1
        elif cmd == 3:
            if queueLen == 0:
                print(-1)
            else:
                print(queue.popleft())
                queueLen -= 1
        elif cmd == 4:
            if queueLen == 0:
                print(-1)
            else:
                print(queue.pop())
                queueLen -= 1
        elif cmd == 5:
            print(queueLen)
        elif cmd == 6:
            if queueLen == 0:
                print(1)
            else:
                print(0)
        elif cmd == 7:
            if queueLen == 0:
                print(-1)
            else:
                data = queue.popleft()
                print(data)
                queue.appendleft(data)
        elif cmd == 8:
            if queueLen == 0:
                print(-1)
            else:
                data = queue.pop()
                print(data)
                queue.append(data)

main()