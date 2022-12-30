import sys

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())

    addressDict = {}

    for i in range(0, n):
        dataList = list(sys.stdin.readline().rstrip().split())

        address = dataList[0]
        password = dataList[1]

        addressDict[address] = password

    for j in range(0, m):
        needAddress = sys.stdin.readline().rstrip()

        print(addressDict[needAddress])

# __main__
main()