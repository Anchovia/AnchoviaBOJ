def main():
    resultMoney = 0

    targetMoney = int(input())
    testCase = int(input())

    for _ in range(testCase):
        money, amount = map(int, input().split())
        resultMoney += money * amount

    
    if resultMoney == targetMoney : print("Yes")
    else: print("No")

main()