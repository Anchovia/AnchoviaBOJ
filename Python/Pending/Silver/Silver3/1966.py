import sys

def singleIntegerInput():
    n = int(sys.stdin.readline())

    return n

def doubleIntegerInput():
    a, b = map(int, sys.stdin.readline().split())

    return a, b

def listIntegerInput():
    l = list(map(int, sys.stdin.readline().split()))

    return l

def findInportance(needsIndex, importanceList):
    count = 1

    while True:
        maximumImportance = max(importanceList)
      
        nowData = importanceList[0]

        if(nowData == maximumImportance):
            if(needsIndex == 0):
                return count

            else:
                del importanceList[0]

                count += 1
        
        else:
            importanceList.append(nowData)
            del importanceList[0]
        
        needsIndex -= 1

        if(needsIndex < 0):
            needsIndex = len(importanceList) - 1

def printList(l):
    for i in l:
        print(i)

def main():
    resultList = []

    case = singleIntegerInput()

    for i in range(0, case):
        document, needsIndex = doubleIntegerInput()
        importanceList = listIntegerInput()

        result = findInportance(needsIndex, importanceList)

        resultList.append(result)

    printList(resultList)

# __main()__
main()