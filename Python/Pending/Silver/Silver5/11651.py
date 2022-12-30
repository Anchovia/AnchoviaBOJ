import sys

# 점의 갯수 인풋 함수
def numberOfPointInput():
    n = int(input())

    return n

def pointInput(n):
    pointList = []

    for i in range(0, n):
        x, y = input().split()
        data = [int(y), int(x)]

        pointList.append(data)

    return pointList

def swapList(pointList):
    for i in pointList:
        i[0], i[1] = i[1], i[0]

    return pointList

def printList(pointList):
    for i in pointList:
        print(i[0], i[1])


# main()
def main():
    n = numberOfPointInput()

    pointList = pointInput(n)
    pointList.sort()
    pointList = swapList(pointList)

    printList(pointList)

main()
