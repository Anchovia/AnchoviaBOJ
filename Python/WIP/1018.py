from sys import stdin

def solution(dataList, m, n):
    minResult = 2500
    result = 0
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    judgList = [[False for _ in range(n)] for _ in range(m)]
    for x in range(m):
        for y in range(n):
            pass
        

def main():
    m, n = map(int, input().split())
    dataList = [stdin.readline().rstrip() for _ in range(m)]
    solution(dataList, m, n)

main()