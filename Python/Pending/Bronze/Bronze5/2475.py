import sys

def main():
    dataList = list(map(int, sys.stdin.readline().rstrip().split()))

    rawResult = 0

    for i in dataList:
        rawResult += i ** 2
    
    print(rawResult % 10)

# __main__
main()