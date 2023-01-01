import sys

def doubleDataInputFunc():
    data1, data2 = map(int, sys.stdin.readline().rstrip().split())

    return data1, data2

def main():
    n, k = doubleDataInputFunc()

# __main__
main()