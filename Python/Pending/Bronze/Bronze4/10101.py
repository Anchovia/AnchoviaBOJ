def solution(dataList):
    sumAll, equipCount = sum(dataList), 0

    if dataList[0] == dataList[1]:
        equipCount += 1
    if dataList[0] == dataList[2]:
        equipCount += 1
    if dataList[1] == dataList[2]:
        equipCount += 1
    
    if sumAll == 180 and equipCount == 3:
        return "Equilateral"
    elif sumAll == 180 and equipCount == 1:
        return "Isosceles"
    elif sumAll == 180:
        return "Scalene"
    else:
        return "Error"

def main():
    dataList = [int(input()) for _ in range(3)]
    resultStrs = solution(dataList)
    print(resultStrs)

main()