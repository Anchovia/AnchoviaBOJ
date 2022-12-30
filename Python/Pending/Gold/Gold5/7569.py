import sys

def findIdx(tomatoList, m, n, h):
    tomatoIdxList = []

    tomatoSize = 0
    blankSize = 0

    z = 0

    while(z < h):
        y = 0

        while(y < n):
            x = 0
            
            while(x < m):
                if(tomatoList[z][y][x] == 1):
                    tomatoIdxList.append([z, y, x])
                    tomatoSize += 1
                
                elif(tomatoList[z][y][x] == -1):
                    blankSize += 1
                
                x += 1
            
            y += 1
        
        z += 1
    
    return tomatoIdxList, tomatoSize, blankSize

def findDays(tomatoList, m, n, h):
    days = 0

    tomatoIdxList, tomatoSize, blankSize = findIdx(tomatoList, m, n, h)

    listSize = m * n * h
    rawSize = listSize - blankSize
    beforeRawSize = -1
    
    while True:
        if(tomatoSize + blankSize == listSize):
            return days

        elif(beforeRawSize == rawSize):
            return -1

        else:
            beforeRawSize = rawSize
            newIdx = []

            for nowIdxList in tomatoIdxList:
                x = nowIdxList[2]
                y = nowIdxList[1]
                z = nowIdxList[0]

                up = [z, y - 1, x]
                down = [z, y + 1, x]
                left = [z, y, x - 1]
                right = [z, y, x + 1]
                top = [z + 1, y, x]
                botton = [z - 1, y, x]

                dataList = [up, down, left, right, top, botton]

                for nowIdx in dataList:
                    nowX = nowIdx[2]
                    nowY = nowIdx[1]
                    nowZ = nowIdx[0]

                    if(nowX < 0 or nowY < 0 or nowZ < 0 or nowX >= m or nowY >= n or nowZ >= h):
                        continue
                                
                    if(tomatoList[nowZ][nowY][nowX] == 0):
                        tomatoList[nowZ][nowY][nowX] = 1
                        newIdx.append([nowZ, nowY, nowX])

                        tomatoSize += 1
                        rawSize -= 1

                    else:
                        pass

            tomatoIdxList = newIdx

            days += 1

def main():
    m, n, h = map(int, sys.stdin.readline().rstrip().split())

    tomatoList = []

    for i in range(0, h):
        rawDataList = []

        for j in range(0, n):
            dataList = list(map(int, sys.stdin.readline().rstrip().split()))

            rawDataList.append(dataList)
        
        tomatoList.append(rawDataList)

    days = findDays(tomatoList, m, n, h)

    print(days)

# __main__
main()