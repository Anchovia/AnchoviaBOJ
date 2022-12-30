import sys

def findNumber(dataList, needFindNumber):
    frontIdx = 0
    lastIdx = len(dataList) - 1
    midIdx = (lastIdx - frontIdx) // 2

    pastMidIdx = ''

    while(needFindNumber != dataList[midIdx]):
        if(pastMidIdx == midIdx):
            return 0

        elif(needFindNumber < dataList[midIdx]):
            lastIdx = midIdx - 1
            
        elif(needFindNumber > dataList[midIdx]):
            frontIdx = midIdx + 1

        pastMidIdx = midIdx
        
        midIdx = (lastIdx - frontIdx) // 2 + frontIdx
        
    return 1
    
def main():
    n = int(sys.stdin.readline().rstrip())

    dataList = list(map(int, sys.stdin.readline().rstrip().split()))
    dataList.sort()

    m = int(sys.stdin.readline().rstrip())

    needFindList = list(map(int, sys.stdin.readline().rstrip().split()))

    for needFindNumber in needFindList:
        result = findNumber(dataList, needFindNumber)
        print(result)

# __main__
main()