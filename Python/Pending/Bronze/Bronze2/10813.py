def main():
    size, testCase = map(int, input().split())
    dataList = list()

    for i in range(size + 1):
        dataList.append(i)

    for _ in range(testCase):
        a, b = map(int, input().split())
        dataList[a], dataList[b] = dataList[b], dataList[a]

    dataList.pop(0)

    print(" ".join(str(i) for i in dataList))

main()