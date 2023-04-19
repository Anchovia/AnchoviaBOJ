def main():
    target, word = map(int, input().split())

    dataList = list(input().split())

    consonantList = list()
    vowelList = list()
    
    for nowStr in dataList:
        if nowStr == "a" or nowStr == "e" or nowStr == "i" or nowStr == "o" or nowStr == "u":
            vowelList.append(nowStr)
        else:
            consonantList.append(nowStr)

    consonantList.sort()
    vowelList.sort()

    print(consonantList)
    print(vowelList)

main()