import sys

def solution(dataList):
    dataList.sort(reverse=True)
    print(dataList)

def main():
    dataList = list()

    testCase = int(input())

    for _ in range(testCase):
        weight, height = map(int, sys.stdin.readline().rstrip().split())
        dataList.append([weight, height])

    solution(dataList)

# __main__
main()