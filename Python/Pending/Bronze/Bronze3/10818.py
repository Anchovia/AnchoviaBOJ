import sys

def main():
    n = int(sys.stdin.readline().rstrip())

    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    dataList.sort()

    print(dataList[0], dataList[len(dataList) - 1])

# __main__
main()