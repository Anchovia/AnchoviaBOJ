from collections import deque

def solution(dataList, n):
    dataQueue = deque(dataList)
    resultIdxs = [0 for _ in range(2001)]
    queueLen = n
    count = 1
    while queueLen > 0:
        now = dataQueue.popleft()
        resultIdxs[now] = count
        queueLen -= 1
        count += 1
    
    resultList = [resultIdxs[now] for now in dataList]
    return resultList

def printFunc(resultList, n):
    for i in range(1, n + 1):
        if i != n:
            print(resultList[i - 1], end = " ")
        else:
            print(resultList[i - 1])

def main():
    n = int(input())
    dataList = list(map(int, input().split()))
    resultList = solution(dataList, n)
    printFunc(resultList, n)

main()