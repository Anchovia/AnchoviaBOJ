def solution(dataList):
    dataList.sort()
    result = dataList[0] + dataList[1]

    if result <= dataList[2]:
        result += result - 1
    else:
        result += dataList[2]
    
    return result

def main():
    dataList = list(map(int, input().split()))
    result = solution(dataList)
    print(result)

main()