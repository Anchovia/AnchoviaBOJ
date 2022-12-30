import sys

def singleDataInputFunc():
    data = int(sys.stdin.readline().strip())

    return data

def doubleDataInputFunc():
    data1, data2 = map(int, sys.stdin.readline().rstrip().split())

    return data1, data2

def dataListInputFunc():
    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    return dataList

