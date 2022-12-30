import sys

def main():
    n, k = map(int, sys.stdin.readline().rstrip().split())

    numberList = list(map(int, sys.stdin.readline().rstrip().split()))

    numberList.sort()

    print(numberList[k - 1])

# __main__
main()