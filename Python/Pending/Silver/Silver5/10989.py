import sys

def main():
    dataList = [0] * 10000

    n = int(sys.stdin.readline().rstrip())

    for i in range(0, n):
        data = int(sys.stdin.readline())

        dataList[data - 1] += 1

    for k in range(0, len(dataList)):
        if(dataList[k] != 0):
            for i in range(0, dataList[k]):
                print(k + 1)
        
        else:
            pass

# __main__
main()