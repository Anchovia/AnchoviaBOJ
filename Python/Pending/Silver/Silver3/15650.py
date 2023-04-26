from itertools import permutations

def main():
    maximum, selector = map(int, input().split())

    selectorList = [i for i in range(1, maximum + 1)]

    permutationList = permutations(selectorList, selector)

    resultList = list()
    resultStr = ""

    for nowTuple in permutationList:
        nowList = list(nowTuple)
        nowList.sort()
        nowStr = str(nowList).strip("[]").replace(",", "")
        if str(nowStr) + "\n" not in resultList:
            resultList.append(nowStr + "\n")
        else:
            pass
    
    for i in resultList:
        resultStr += i

    print(resultStr, end="")

main()