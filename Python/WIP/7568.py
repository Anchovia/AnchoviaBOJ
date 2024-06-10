from sys import stdin

def main():
    n = int(input())
    dataList = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

main()