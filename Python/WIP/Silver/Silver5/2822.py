def main():
    dataList = list()
    resultList = list()
    sum = 0

    for i in range(1, 9):
        data = int(input())

        dataList.append([data, i])

    dataList.sort()

    for j in range(5):
        sum += dataList[j][0]
        resultList.append(dataList[j][1])
    
    print(sum)
    print(dataList)

# __main__
main()