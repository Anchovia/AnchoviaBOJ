from sys import stdin

def solution(dataList):
    dataList = list(set(dataList))
    dataList.sort()
    dataDict = {now : i for i, now in enumerate(dataList)}
    return dataDict

def main():
    n = int(input())
    dataList = list(map(int, stdin.readline().rstrip().split()))
    dataDict = solution(dataList)
    count = 1
    for now in dataList:
        if count == n:
            print(dataDict[now])
        else:
            print(dataDict[now], end=" ")
            count += 1

main()