from collections import deque

def solution(n):
    queue = deque(i for i in range(1, n + 1))
    logic = True
    while len(queue) != 1:
        if logic == True:
            queue.popleft()
            logic = False
        else:
            data = queue.popleft()
            queue.append(data)
            logic = True
    return queue[0]

def main():
    n = int(input())
    
    result = solution(n)

    print(result)

main()