# module import
import sys

def dataListInputFunc(people):
    dataList = list()

    for idx in range(people):
        age, name = map(str, sys.stdin.readline().rstrip().split())

        dataList.append([int(age), int(idx), name])

    return dataList

def printFunc(dataList):
    for nowData in dataList:
        print(nowData[0], nowData[2])


def main():
    people = int(input())

    dataList = dataListInputFunc(people)

    dataList.sort()

    printFunc(dataList)

# __main__
main()