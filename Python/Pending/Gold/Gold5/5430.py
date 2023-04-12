import sys
from collections import deque

def queuePrint(dataQueue):
    printStr = "["

    for i in range(len(dataQueue)):
        nowData = str(dataQueue.popleft())

        if len(dataQueue) == 0:
            printStr += nowData + "]"
        else:
            printStr += nowData + ","
    
    print(printStr)

def TransformStrToDeque(dataQueue):
    newQueue = deque()
    numberStr = ""

    for nowStr in dataQueue:
        if nowStr == '[' or nowStr == ']' or nowStr == ',':
            if len(numberStr) > 0:
                newQueue.append(int(numberStr))
                numberStr = ""
        else:
            numberStr += nowStr

    return newQueue

def acFunc(funcStrs, dataLength, dataQueue):
    reverseCount = 0

    for nowFunc in funcStrs:
        if nowFunc == 'R':
            reverseCount += 1
        elif nowFunc == 'D':
            if dataLength == 0:
                print("error")
                return 1

            if reverseCount % 2 == 0:
                dataQueue.popleft()
                dataLength -= 1
            else:
                dataQueue.pop()
                dataLength -= 1
    
    if dataLength == 0:
        print("[]")
    else:
        if reverseCount % 2 == 0:
            queuePrint(dataQueue)
        else:
            dataQueue.reverse()
            queuePrint(dataQueue)

def solution(testCase):
    for _ in range(testCase):
        funcStrs = sys.stdin.readline().rstrip()
        dataLength = int(sys.stdin.readline().rstrip())
        dataQueue = sys.stdin.readline().rstrip()

        dataQueue = TransformStrToDeque(dataQueue)

        acFunc(funcStrs, dataLength, dataQueue)

def main():
    testCase = int(input())

    solution(testCase)
    
main()