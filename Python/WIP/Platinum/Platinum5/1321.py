def main():
    armyList = [0] * 500001

    army = int(input())

    soldierList = map(int, input().split())

    for nowData in soldierList:
        armyList[nowData] = nowData

    testCase = int(input())

    for _ in range(testCase):
        pass

main()