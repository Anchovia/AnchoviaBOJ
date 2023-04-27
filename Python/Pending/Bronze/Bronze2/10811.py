def main():
    size, testCase = map(int, input().split())
    dataList = list()

    for i in range(size + 1):
        dataList.append(i)

    for _ in range(testCase):
        newList = list()
        start, end = map(int, input().split())

        for j in range(start, end + 1):
            newList.append(dataList[j])
        
        for k in range(start, end + 1):
            dataList[k] = newList.pop()
    
    dataList.pop(0)

    print(" ".join(str(i) for i in dataList))

main()