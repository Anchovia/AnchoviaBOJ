def solution(n, dataList):
    maxArea = n * 100
    result = maxArea
    return result

def main():
    n = int(input())
    dataList = [list(map(int, input().split())) for _ in range(n)]
    result = solution(n, dataList)
    print(result)

main()