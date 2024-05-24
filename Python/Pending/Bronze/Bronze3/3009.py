def solution(dataList):
    xList, yList = [], []
    allXList, allYList = [], []
    x, y = 0, 0
    for now in dataList:
        if now[0] in xList:
            pass
        else:
            xList.append(now[0])

        if now[1] in yList:
            pass
        else:
            yList.append(now[1])
        
        allXList.append(now[0])
        allYList.append(now[1])
    
    if allXList.count(xList[0]) == 2:
        x = xList[1]
    else:
        x = xList[0]
    
    if allYList.count(yList[0]) == 2:
        y = yList[1]
    else:
        y = yList[0]

    return x, y
        
def main():
    dataList = [list(map(int, input().split())) for _ in range(3)]
    x, y = solution(dataList)
    print(f"{x} {y}")

main()