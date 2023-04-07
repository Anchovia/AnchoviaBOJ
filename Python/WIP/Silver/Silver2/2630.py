import sys

def dataListInputFunc(length):
    dataList = list()

    for _ in range(length):
        lawDataList = sys.stdin.readline().rstrip().split()
        dataList.append(lawDataList)

    return dataList

def searchFunc(dataList):
    pass

def main():
    length = int(input())

    dataList = dataListInputFunc(length)

    searchFunc(dataList)

    print(dataList)

# __main__
main()