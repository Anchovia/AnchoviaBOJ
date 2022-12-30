import sys

def findTomatoIdx(tomatoList, m, n):
    tomatoIdxList = []

    tomatoSize = 0
    blankSize = 0

    y = 0
    while(y < n):
        x = 0

        while(x < m):
            if(tomatoList[y][x] == 1):
                tomatoIdxList.append([y, x])
                tomatoSize += 1
            
            elif(tomatoList[y][x] == -1):
                blankSize += 1
            
            x += 1

        y += 1

    return tomatoIdxList, tomatoSize, blankSize

def runMakeTomato(tomatoList, m, n):
    days = 0

    tomatoIdxList, tomatoSize, blankSize = findTomatoIdx(tomatoList, m, n)

    listSize = m * n
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
                x = nowIdxList[1]
                y = nowIdxList[0]

                up = [y - 1, x]
                down = [y + 1, x]
                left = [y, x - 1]
                right = [y, x + 1]

                dataList = [up, down, left, right]

                for nowIdx in dataList:
                    nowY = nowIdx[0]
                    nowX = nowIdx[1]

                    if(nowX < 0 or nowY < 0 or nowX >= m or nowY >= n):
                        continue
                            
                    if(tomatoList[nowY][nowX] == 0):
                        tomatoList[nowY][nowX] = 1
                        newIdx.append([nowY, nowX])

                        tomatoSize += 1
                        rawSize -= 1

                    else:
                        pass

            tomatoIdxList = newIdx

            days += 1

def main():
    tomatoList = []

    m, n = map(int, sys.stdin.readline().rstrip().split())

    for i in range(0, n):
        tomatoList.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    days = runMakeTomato(tomatoList, m, n)
    
    print(days)

# __main__
main()