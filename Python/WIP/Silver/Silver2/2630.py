import sys

def makeMatrix(size):
    matrixList = []
    newList = list()

    for _ in range(size):
        data = sys.stdin.readline().rstrip().split(" ")

        newList.append(data)

    matrixList.append(newList)

    return matrixList

def solution(matrixList, size):
    resultList = list()
    newList = list()

    x, y = 0, 0

    while x < size and y < size:
        for nowList in matrixList:
            temp = nowList[0][0]

            for y in range(size):
                for x in range(1, size):
                    nowData = nowList[y][x]

                    if nowData != temp:
                        size //= 2

                    temp = nowData

    return resultList


def main():
    size = int(input())

    matrixList = makeMatrix(size)

    resultList = solution(matrixList, size)

# __main__
main()