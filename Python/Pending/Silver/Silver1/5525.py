# P1의 경우, IOI 에서 I의 갯수 -1 (IOIOIOIOIOI에서 P1의 값은 5)[I는 6개]
# P2의 경우, IOIOI에서 I의 갯수 -2
# P3의 경우, IOIOIOI에서 I의 갯수 -3
# 즉, IOIOIOIOIOI... 에서 Result는 I의 갯수 - 1

def searchIO(n, strsLength, strs):
    i = 0

    searchedList = list()
    findList = list()

    while i < strsLength:
        nowStr = strs[i]

        findList.append(nowStr)

        if findList[0] == 'O':
            findList.pop(0)
        
        if len(findList) > 1:
            if findList[len(findList) - 2] == 'I':
                if nowStr == 'I':
                    findList.pop(len(findList) - 1)

                    if len(findList) > n * 2:
                        if findList[len(findList) - 1] == 'O':
                            findList.pop(len(findList) - 1)

                        searchedList.append(findList)
                        findList = list()
                    else:
                        findList = list()
                    
                    i -= 1
            elif findList[len(findList) - 2] == 'O':
                if nowStr == 'O':
                    findList.pop(len(findList) - 1)

                    if len(findList) > n * 2:
                        if findList[len(findList) - 1] == 'O':
                            findList.pop(len(findList) - 1)

                        searchedList.append(findList)
                        findList = list()
                    else:
                        findList = list()

                    i -= 1

        i += 1
    
    if len(findList) > n * 2:
        if findList[len(findList) - 1] == 'O':
            findList.pop(len(findList) - 1)

        searchedList.append(findList)
        findList = list()
    return searchedList

def solution(n, searchedList):
    result = 0

    for nowList in searchedList:
        result += (len(nowList) // 2 + 1) - n

    return result

def main():
    n = int(input())
    strsLength = int(input())
    strs = input()

    searchedList = searchIO(n, strsLength, strs)
    result = solution(n, searchedList)

    print(result)

main()