import sys

def singleDataInputFunc():
    data = int(sys.stdin.readline().strip())

    return data

def dataListInputFunc():
    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    return dataList

def main():
    n = singleDataInputFunc()
    timeList = dataListInputFunc()

    timeList.sort()

    temp = 0
    result = 0
    solve = 0

    for i in range(0, len(timeList), 1):
        result = timeList[i] + temp
        temp = result
        solve += result

    print(solve)

# __main__
main()