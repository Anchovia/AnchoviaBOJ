import sys

def singleDataInputFunc():
    data = int(sys.stdin.readline().rstrip())

    return data

def findResult(n):
    result = 0
    nowData = n

    while(nowData > 1):
        if((nowData - 1) + (nowData - 1) == nowData):
            pass

        elif((nowData - 1) + (nowData - 2) == nowData):
            pass


    return result

def main():
    testCase = singleDataInputFunc()

    for i in range(testCase):
        n = singleDataInputFunc()
        print(findResult(n))

# __main__
main()