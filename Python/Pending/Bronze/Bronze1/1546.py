import sys

def main():
    result = 0

    n = int(sys.stdin.readline().rstrip())

    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    maximum = max(dataList)

    for i in dataList:
        result += i / maximum * 100
    
    print(result / n)

# __main__
main()