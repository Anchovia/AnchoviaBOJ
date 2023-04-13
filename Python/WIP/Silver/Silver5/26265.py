def main():
    dataList = list()

    i = int(input())

    for _ in range(i):
        data = list(input().split())
        dataList.append(data)

    dataList.sort()

    print(dataList)

main()