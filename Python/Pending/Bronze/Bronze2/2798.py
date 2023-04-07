from itertools import combinations

def solution(combination, maxSum):
    result = 0

    for nowList in combination:
        nowSolved = sum(nowList)

        if(result < nowSolved <= maxSum):
            result = nowSolved

    return result

def main():
    pickCard, maxSum = map(int, input().split())
    cardData = list(map(int, input().split()))
    combination = list(combinations(cardData, 3))

    result = solution(combination, maxSum)

    print(result)

main()