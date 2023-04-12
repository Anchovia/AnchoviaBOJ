def main():
    dataLength = int(input())

    list_Data = list(map(int, input().split()))

    list_Data.sort()

    strs = ' '.join([str(elem) for elem in list_Data])

    print(strs)

main()