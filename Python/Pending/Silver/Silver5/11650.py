import sys

# 점의 갯수 인풋 함수
def numberOfPointInput():
    n = int(sys.stdin.readline())

    return n

def pointInput(n):
    pointList = []

    for i in range(0, n):
        x, y = map(int, sys.stdin.readline().split())
        data = [x, y]

        pointList.append(data)

    return pointList

def printList(pointList):
    for i in pointList:
        print(i[0], i[1])

# main()
def main():
    n = numberOfPointInput()

    pointList = pointInput(n)
    pointList.sort()

    printList(pointList)

main()
