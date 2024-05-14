def solution(money):
    change = [500, 100, 50, 10, 5, 1]
    count = 0

    for nowChange in change:
        count += money // nowChange
        money = money % nowChange
    
    return count

def __main__():
    money = int(input())
    count = solution(1000 - money)
    print(count)

__main__()