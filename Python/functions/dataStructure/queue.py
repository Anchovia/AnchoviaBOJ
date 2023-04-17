from collections import deque

queue = deque()

# TEST

queue.append(1)
queue.appendleft(2)
queue.append(3)
queue.append(4)
queue.appendleft(5)
queue.appendleft(6)

queue.pop()
queue.popleft()

print(queue)