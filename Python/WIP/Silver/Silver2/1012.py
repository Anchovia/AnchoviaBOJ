import sys

def singleDataInput():
    data = int(sys.stdin.readline().strip())

    return data

def doubleDataInput():
    data1, data2 = map(int, sys.stdin.readline().rstrip().split())

    return data1, data2

def dataListInput():
    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    return dataList

def trasferToData(dataList):
    M = dataList[0]
    N = dataList[1]
    K = dataList[2]

    return M, N, K

def searchData(indexList, K):
    count = 0

    for i in range(K):
        x = indexList[0][0]
        y = indexList[0][1]

        if [x + 1, y] in indexList:
            indexList.pop(0)

        elif [x - 1, y] in indexList:
            indexList.pop(0)

        elif [x, y + 1] in indexList:
            indexList.pop(0)

        elif [x, y - 1] in indexList:
            indexList.pop(0)

        else:
            count += 1
            indexList.pop(0)
    
    return count

def __main__():
    testCase = singleDataInput()

    for i in range(testCase):
        indexList = []

        dataList = dataListInput()
        M, N, K = trasferToData(dataList)

        for j in range(K):
            x, y = doubleDataInput()
            indexList.append([x, y])
        
        count = searchData(indexList, K)

        print(count)

__main__()