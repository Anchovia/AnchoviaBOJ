import sys
from itertools import combinations

def main():
    dataList = list()

    case = int(input())

    for _ in range(case):
        data = list(map(int, sys.stdin.readline().rstrip().split()))

        dataList.append(data)

    combinationList = list(combinations(dataList, 2))

    print(combinationList)

main()