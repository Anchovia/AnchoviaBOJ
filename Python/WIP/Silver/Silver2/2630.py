import sys

def singleDataInputFunc():
    data = int(sys.stdin.readline().rstrip())

    return data

def dataListInputFunc():
    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    return dataList

def divideListFunc(dataList):
    newList = []

    for nowList in dataList:
        newList.append(nowList[:len(nowList) // 2])
        newList.append(nowList[len(nowList) // 2:])

    return newList


def findResult(idxList):
    white = 0
    blue = 0

    judg = True

    for x in range(0, len(idxList)):
        if(judg):
            break

        for y in range(0, len(idxList[x])):
            if(idxList[x][y] == 0):
                judg = False
                break



    return white, blue

def main():
    n = singleDataInputFunc()
    idxList = []

    for i in range(n):
        dataList = dataListInputFunc()
        idxList.append(dataList)
    
    white, blue = findResult(idxList)

    print(white)
    print(blue)

# __main__
main()