def main():
    n, k = map(int, input().split())
    scoreList = list(map(int, input().split()))
    scoreList.sort()
    print(scoreList[n - k])

main()