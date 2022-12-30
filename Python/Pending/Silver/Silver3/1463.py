import sys

def singleDataInputFunc():
    data = int(sys.stdin.readline().strip())

    return data

def findMinData(x):
    if(x == 1):
        return 0
    
    else:
        judg = True

        dataList = [[x]]

        while(judg):
            resultList = []
            for nowData in dataList[len(dataList) - 1]:
                resultList, judg = minusFunc(nowData, resultList, judg)
                resultList, judg = divTwoFunc(nowData, resultList, judg)
                resultList, judg = divThreeFunc(nowData, resultList, judg)
            
            resultList = set(resultList)
            resultList = list(resultList)
            
            dataList.append(resultList)

        return len(dataList) - 1

def minusFunc(nowData, resultList, judg):
    data = nowData - 1
    resultList.append(data)

    if(data == 1):
            judg = False

    return resultList, judg

def divTwoFunc(nowData, resultList, judg):
    if(nowData % 2 == 0):
        data = nowData // 2
        resultList.append(data)

        if(data == 1):
            judg = False

        return resultList, judg
    
    else:
        return resultList, judg

def divThreeFunc(nowData, resultList, judg):
    if(nowData % 3 == 0):
        data = nowData // 3
        resultList.append(data)

        if(data == 1):
            judg = False

        return resultList, judg
    
    else:
        return resultList, judg

def main():
    x = singleDataInputFunc()

    print(findMinData(x))

# __main__
main()