def solution(dataList, n):
    lrudDict = {'L' : 0, 'R' : 1, 'U' : 2, 'D' : 3}
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    x, y = 1, 1

    for now in dataList:
        idx = lrudDict[now]
        if x + dx[idx] > 0 and y + dy[idx] > 0 and x + dx[idx] <= n and y + dy[idx] <= n:
            x, y = x + dx[idx], y + dy[idx]
    
    return x, y

def main():
    n = int(input())
    dataList = input().split()
    x, y = solution(dataList, n)
    print(x, y)

main()