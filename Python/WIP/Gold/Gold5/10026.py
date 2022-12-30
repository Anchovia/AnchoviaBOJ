import sys

def findIdx(graphicsList, n):
    redIdxList = []
    greenIdxList = []
    blueIdxList = []

    y = 0

    while(y < n):
        x = 0

        while(x < n):
            if(graphicsList[y][x] == 'R'):
                redIdxList.append([y, x])
            
            elif(graphicsList[y][x] == 'G'):
                greenIdxList.append([y, x])
            
            elif(graphicsList[y][x] == 'B'):
                blueIdxList.append([y, x])

            x += 1

        y += 1
    
    return redIdxList, greenIdxList, blueIdxList

def searchColorCount(colorIdxList, color):
    count = 0
    
    for nowIdx in colorIdxList:
        nowY = nowIdx[0]
        nowX = nowIdx[1]

        up = [nowY - 1, nowX]
        down = [nowY + 1, nowX]
        left = [nowY, nowX - 1]
        right = [nowY, nowX + 1]

        needSearchArrow = [up, down, left, right]

        for nowFound in needSearchArrow:
            foundY = nowFound[0]
            foundX = nowFound[1]

            if(colorIdxList[foundY][foundX] == color or colorIdxList[foundY][foundX] == (color + 'C')):
                123

def main():
    n = int(sys.stdin.readline().rstrip())

    graphicsList = []

    for i in range(0, n):
        dataList = list(sys.stdin.readline().rstrip())
        graphicsList.append(dataList)
    
    redIdxList, greenIdxList, blueIdxList = findIdx(graphicsList, n)

# __main__
main()