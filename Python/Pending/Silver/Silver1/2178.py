import copy
from collections import deque

def makeMatrix(height, width):
    matrixList = list()
    indexList = list()

    for y in range(height):
        rawList = list()

        dataStr = input()

        for x in range(width):
            nowStr = dataStr[x]

            if nowStr == "1":
                indexList.append([y, x])

            rawList.append(nowStr)
        
        matrixList.append(rawList)
    
    return matrixList, indexList

def solution(matrixList, indexList, height, width):
    result = 0
    count = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = {tuple(i) : False for i in indexList}

    queue = deque([[0, 0]])

    while queue:
        cnt = count
        count = 0
        
        for _ in range(cnt):
            nowData = queue.popleft()
        
            x, y = nowData[1], nowData[0]
            visited[(y, x)] = True

            for i in range(4):
                nowX, nowY = x + dx[i], y + dy[i]

                if [nowY, nowX] == [height - 1, width - 1]:
                    return result + 2

                if nowX < 0 or nowY < 0 or nowX > width - 1 or nowY > height - 1:
                    pass

                else:
                    if matrixList[nowY][nowX] == "1" and not visited[(nowY, nowX)]\
                            and [nowY, nowX] not in queue:

                        queue.append([nowY, nowX])
                        count += 1
            
        result += 1

    return result


def main():
    height, width = map(int, input().split())

    matrixList, indexList = makeMatrix(height, width)
    result = solution(matrixList, indexList, height, width)

    print(result)

main()