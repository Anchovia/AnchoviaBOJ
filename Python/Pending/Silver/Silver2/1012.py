import sys
from collections import deque

def bfs(indexList, startIdx):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    findQueue = deque([startIdx])
    resultQueue = deque([])

    while findQueue:
        nowIdx = findQueue.popleft()
        
        x = nowIdx[0]
        y = nowIdx[1]

        for i in range(4):
            if [x + dx[i], y + dy[i]] in indexList and [x + dx[i], y + dy[i]] not in resultQueue and [x + dx[i], y + dy[i]] not in findQueue:
                findQueue.append([x + dx[i],  y + dy[i]])
        
        resultQueue.append([x, y])

    for nowIdx in resultQueue:
        indexList.remove(nowIdx)

    return indexList

def makeIndexList(indexAmount):
    indexList = list()

    for _ in range(indexAmount):
        x, y = map(int, sys.stdin.readline().rstrip().split())

        indexList.append([x, y])
    
    return indexList

def solution():
    count = 0

    width, height, indexAmount = map(int, sys.stdin.readline().rstrip().split())

    indexList = makeIndexList(indexAmount)

    while indexList:
        startIdx = indexList[0]
        indexList = bfs(indexList, startIdx)
        count += 1
    
    return count

def __main__():
    testCase = int(sys.stdin.readline())

    for _ in range(testCase):
        count = solution()
        print(count)

__main__()