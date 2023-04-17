from collections import deque

def makeMatrix(size):
    normalMatrix = list()
    specialMatrix = list()

    normalIndexDict = {
        'R' : [],
        'G' : [],
        'B' : []
    }
    specialIndexDict = {
        'R' : [],
        'B' : []
    }

    for y in range(size):
        nowStr = input() # 데이터 인풋

        specialMatrixRawList = list()

        for x in range(size):
            if nowStr[x] == 'R' or nowStr[x] == 'G':
                specialMatrixRawList.append('R')
                specialIndexDict['R'].append([x, y])
            else:
                specialMatrixRawList.append('B')
                specialIndexDict['B'].append([x, y])
            
            normalIndexDict[nowStr[x]].append([x, y])

        normalMatrix.append(nowStr)
        specialMatrix.append(specialMatrixRawList)

    return normalMatrix, specialMatrix, normalIndexDict, specialIndexDict

def bfs(matrixList, indexDict, size):
    solution = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for key in indexDict.keys():
        colorList = indexDict[key]

        # searchedDict 생성
        searchedDict = dict()

        for idx in colorList:
            searchedDict[str(idx)] = False

        for nowIdx in range(len(colorList)):
            # startIdx 및 needFindQueue 생성
            startIdx = colorList[nowIdx]
            startX, startY = startIdx[0], startIdx[1]

            if searchedDict[str(startIdx)] == True:
                continue
            else:
                needFindQueue = deque([[startX, startY]])

                # needFindQueue가 빌 때 까지 반복
                while needFindQueue:
                    nowIdx = needFindQueue.popleft()

                    x, y = nowIdx[0], nowIdx[1]

                    searchedDict[str([x, y])] = True
                    
                    for i in range(4):
                        nowX, nowY = x + dx[i], y + dy[i]

                        if nowX < 0 or nowY < 0 or nowX > size - 1 or nowY > size - 1:
                            pass
                        else:
                            if matrixList[nowY][nowX] == key:
                                if not searchedDict[str([nowX, nowY])]:
                                    if [nowX, nowY] not in needFindQueue:
                                        needFindQueue.append([nowX, nowY])
                    
                solution += 1

    return solution

def main():
    size = int(input())
    normalMatrix, specialMatrix, normalIndexDict, specialIndexDict = makeMatrix(size)

    normalMatrixSolution = bfs(normalMatrix, normalIndexDict, size)
    specialMatrixSolution = bfs(specialMatrix, specialIndexDict, size)

    print(f"{normalMatrixSolution} {specialMatrixSolution}")

main()