import sys

def singleDataInputFunc():
    data = int(sys.stdin.readline().rstrip())

    return data

def main():
    testCase = singleDataInputFunc()

    for i in range(testCase):
        n = singleDataInputFunc()

# __main__
main()