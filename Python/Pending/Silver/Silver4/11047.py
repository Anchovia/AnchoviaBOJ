def makeCoinTypeList(coinType):
    CoinTypeList = list()
    
    for _ in range(coinType):
        data = int(input())
        CoinTypeList.append(data)

    return CoinTypeList

def solution(CoinTypeList, targetValue):
    result = 0
    money = targetValue

    while money > 0:
        for i in range(len(CoinTypeList) - 1, -1, -1):
            nowCoinType = CoinTypeList[i]

            while True:
                if nowCoinType <= money:
                    nowMoneyResult = money // nowCoinType
                    
                    money -= nowMoneyResult * nowCoinType
                    result += nowMoneyResult
                else:
                    break

    return result

def main():
    coinType, targetValue = map(int, input().split())

    CoinTypeList = makeCoinTypeList(coinType)

    result = solution(CoinTypeList, targetValue)

    print(result)

# __main__
main()