def main():
    case = int(input())

    dataList = list(map(int, input().split()))

    target = int(input())

    resultCount = 0

    for i in dataList:
        if i == target:
            resultCount += 1

    print(resultCount)

main()