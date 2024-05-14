def solution(dataList):
    change = [25, 10, 5, 1]
    result = [0, 0, 0, 0]
    for nowValue in dataList:
        for i in range(4):
            result[i] = nowValue // change[i]
            nowValue %= change[i]
        print(f"{result[0]} {result[1]} {result[2]} {result[3]}")
        result = [0, 0, 0, 0]

def main():
    testCase = int(input())
    dataList = [int(input()) for _ in range(testCase)]
    solution(dataList)

main()