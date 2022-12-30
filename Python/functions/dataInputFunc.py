import sys

def singleDataInput():
    data = int(sys.stdin.readline().strip())

    return data

def doubleDataInput():
    data1, data2 = map(int, sys.stdin.readline().rstrip().split())

    return data1, data2

def dataListInput():
    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    return dataList

