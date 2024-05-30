def solution(n):
    for nowNum in range(1, n + 1):
        checkNum = 0
        for i in str(nowNum):
            checkNum += int(i)
        checkNum += nowNum
        if checkNum == n:
            return nowNum
    return 0

def main():
    n = int(input())
    result = solution(n)
    print(result)

main()