def solution(numberStr, n):
    result = 0
    numberStr = numberStr[::-1]
    for i, nowNumber in enumerate(numberStr):
        if nowNumber.isalpha():
            nowNumber = ord(nowNumber) - 55
        else:
            nowNumber = int(nowNumber)
        result += nowNumber * (n ** i)
    
    return result

def main():
    numberStr, n = input().split()
    result = solution(numberStr, int(n))
    print(result)

main()