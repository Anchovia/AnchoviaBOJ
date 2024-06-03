from sys import stdin

def solution(coorList):
    minX, maxX = 10001, -10001
    minY, maxY = 10001, -10001
    for nowCoor in coorList:
        x, y = nowCoor[0], nowCoor[1]
        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y

    return (maxX - minX) * (maxY - minY)

def main():
    n = int(input())
    coorList = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
    result = solution(coorList)
    print(result)

main()