from collections import deque
import sys

def main():
    testCase = int(input())
    size = 0

    queue = deque([])

    for _ in range(testCase):
        cmd = sys.stdin.readline().rstrip()

        if cmd[0] == "p" and cmd[1] == "u":
            strs, data = cmd.split(" ")
            queue.append(int(data))
            size += 1

        elif cmd == "front":
            if size > 0:
                print(queue[0])
            else:
                print(-1)
        
        elif cmd == "back":
            if size > 0:
                print(queue[-1])
            else:
                print(-1)
        
        elif cmd == "size":
            print(size)

        elif cmd == "empty":
            if size == 0:
                print(1)
            else:
                print(0)
        
        elif cmd == "pop":
            if size > 0:
                print(queue.popleft())
                size -= 1
            else:
                print(-1)

main()