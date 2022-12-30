import sys

def doubleDataInputFunc():
    data1, data2 = map(int, sys.stdin.readline().rstrip().split())

    return data1, data2

def singleDataInputFunc():
    data = sys.stdin.readline().strip()

    return data

def binary_search(target, dataList):
    start = 0
    end = len(dataList) - 1

    while(start <= end):
        mid = (start + end) // 2

        if(dataList[mid] == target):
            return True
        
        elif(dataList[mid] < target):
            start = mid + 1
        
        else:
            end = mid - 1

    return False

def findResultFunc(hearList, seeList):
    resultList = []
    hearList.sort()

    for nowData in seeList:
        if(binary_search(nowData, hearList)):
            resultList.append(nowData)
    
    return resultList

def main():
    hearList = []
    seeList = []

    resultList = []

    hear, see = doubleDataInputFunc()

    for i in range(hear):
        hearList.append(singleDataInputFunc())
    
    for j in range(see):
        seeList.append(singleDataInputFunc())

    resultList = findResultFunc(hearList, seeList)
    resultList.sort()

    print(len(resultList))

    for result in resultList:
        print(result)

# __main__
main()