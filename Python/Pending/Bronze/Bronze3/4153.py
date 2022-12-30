import sys

def dataInput():
    l = list(map(int, sys.stdin.readline().split()))

    return l

def main():
    while True:
        dataList = dataInput()

        maximum = max(dataList)

        if(maximum == 0):
            break

        idx = dataList.index(maximum)

        del dataList[idx]

        if(maximum == 0):
            break

        if(maximum ** 2 == dataList[0] ** 2 + dataList[1] ** 2):
            print("right")
        
        else:
            print("wrong")

# __main__
main()