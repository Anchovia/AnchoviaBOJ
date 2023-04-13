import sys

def solution():
    result = 0
    cloTypeList = list()

    n = int(sys.stdin.readline())

    for _ in range(n):
        name, cloType = sys.stdin.readline().rstrip().split()
        cloTypeList.append(cloType)

    print(cloTypeList)

    return result

def main():
    testCase = int(sys.stdin.readline())

    for _ in range(testCase):
        result = solution()

        print(result)

main()