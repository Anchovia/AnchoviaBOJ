from collections import deque

# 기준: [y, x]

def makeMatrixList(size):
    matrixList = list()
    indexList = list()

    for y in range(size):
        rawDataList = list()

        data = input()

        for x in range(size):
            nowStr = data[x]

            if nowStr == "1":
                indexList.append([y, x])

            rawDataList.append(nowStr)
        
        matrixList.append(rawDataList)

    return matrixList, indexList

def bfs(matrixList, indexList, size):
    resultList = list()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    searchedDict = dict()
    for nowIdx in indexList:
        searchedDict[str(nowIdx)] = False

    for key in searchedDict.keys():
        if searchedDict[key] == True:
            continue
        else:
            startIdx = list(map(int, key.strip("[]").split(",")))
            needFindQueue = deque([startIdx])
            count = 0

            while needFindQueue:
                nowData = needFindQueue.popleft()
                x, y = nowData[1], nowData[0]
                searchedDict[str([y, x])] = True
                count += 1

                for i in range(4):
                    nowX, nowY = x + dx[i], y + dy[i]

                    if nowX < 0 or nowY < 0 or nowX > size -1 or nowY > size - 1:
                        pass
                    else:
                        if matrixList[nowY][nowX] == '1':
                            if not searchedDict[str([nowY, nowX])]:
                                if [nowY, nowX] not in needFindQueue:
                                    needFindQueue.append([nowY, nowX])

            resultList.append(count)

    return resultList


def main():
    size = int(input())

    matrixList, indexList = makeMatrixList(size)

    resultList = bfs(matrixList, indexList, size)
    resultList.sort()

    print(len(resultList))
    for i in resultList:
        print(i)

main()