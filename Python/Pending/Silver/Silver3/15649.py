from itertools import permutations

def main():
    combinationList = list()
    numberList = list()
    maximum, selector = map(int, input().split())

    for i in range(1, maximum + 1):
        numberList.append(i)

    combinationList = permutations(numberList, selector)

    resultStr = ""
    for nowData in combinationList:
        nowData = list(nowData)
        strs = str(nowData).replace(",", "").strip("[]")
        strs += "\n"
        resultStr += strs

    print(resultStr, end="")

main()