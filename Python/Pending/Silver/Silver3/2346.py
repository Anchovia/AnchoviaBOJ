from collections import deque

def solution(n, dataList):
    resultList = []
    idxList = [i for i in range(1, n + 1)]
    dataQueue = deque(dataList)
    idxList = deque(idxList)
    while n > 0:
        now = dataQueue.popleft()
        idx = idxList.popleft()
        resultList.append(idx)
        n -= 1
        if now > 0:
            dataQueue.rotate(-(now - 1))
            idxList.rotate(-(now - 1))
        else:
            dataQueue.rotate(-now)
            idxList.rotate(-now)
    
    return resultList

def main():
    n = int(input())
    dataList = list(map(int, input().split()))
    resultList = solution(n, dataList)
    print(*resultList)

main()