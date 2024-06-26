from sys import stdin
from collections import deque

def bfs(x, y, m, n, judgList, dataList):
    result = 0
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    queueLen = 1
    queue = deque([[x, y]])

    while queueLen != 0:
        [nowX, nowY] = queue.popleft()
        queueLen -= 1
        judgList[nowX][nowY] = True

        for i in range(4):
            x = nowX + dx[i]
            y = nowY + dy[i]
            if x > -1 and y > -1 and x < m and y < n and judgList[x][y] == False and ([x, y] not in queue):
                queue.append([x, y])
                queueLen += 1
    
    return result


def solution(dataList, m, n):
    judgList = [[False for _ in range(n)] for _ in range(m)]
    minResult = 2500
    # 전체 idx 실행
    for x in range(m):
        for y in range(n):
            nowResult = bfs(x, y, m, n, judgList, dataList)
            if nowResult < minResult:
                minResult = nowResult
    
    return minResult

        

def main():
    m, n = map(int, input().split())
    dataList = [list(stdin.readline().rstrip()) for _ in range(m)]
    minResult = solution(dataList, m, n)
    print(minResult)

main()