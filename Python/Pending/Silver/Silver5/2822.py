def makeDataList():
    dataList = list()

    for _ in range(8):
        data = int(input())

        dataList.append(data)

    return dataList

def makeSortedList(dataList):
    sortedList = list()

    for k in dataList:
        sortedList.append(k)

    sortedList.sort()

    return sortedList

def sumOfList(sortedList):
    sum = 0

    for i in range(3, len(sortedList)):
        sum += sortedList[i]

    return sum

def makeIndexList(dataList, sortedList):
    indexList = list()

    for j in range(3):
        index = dataList.index(sortedList[j])
        indexList.append(index)
    
    indexList.sort()

    return indexList

def printIndexList(indexList):
    strs = ""

    for a in range(0, 8):
        if len(strs) > 6:
            if a in indexList:
                pass
            else:
                strs += str(a + 1)
        else:
            if a in indexList:
                pass
            else:
                strs += str(a + 1) + " "
    
    print(strs)

def main():
    dataList = makeDataList()

    sortedList = makeSortedList(dataList)

    sum = sumOfList(sortedList)

    indexList = makeIndexList(dataList, sortedList)

    print(sum)
    printIndexList(indexList)

main()