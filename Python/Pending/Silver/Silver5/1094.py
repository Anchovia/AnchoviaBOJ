from collections import deque

def sumList(dataList):
    sum = 0

    for i in dataList:
        sum += i

    return sum

def main():
    x = int(input())

    dataList = deque([64])
    findDataList = list()

    sum = 64

    while sum != x:
        nowData = dataList.popleft() // 2
        findDataList.append(nowData)

        if len(dataList) > 0:
            for i in dataList:
                findDataList.append(i)

        sum = sumList(findDataList)

        if sum >= x:
            pass
        else:
            findDataList.append(nowData)
        
        dataList = deque(findDataList)
            
        dataList = deque(sorted(dataList))
        findDataList = list()
        
    print(len(dataList))

main()