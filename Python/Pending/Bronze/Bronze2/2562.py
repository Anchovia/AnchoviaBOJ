import sys

def main():
    numberList = []

    for i in range(0, 9):
        n = int(sys.stdin.readline())

        numberList.append(n)
    
    maximum = max(numberList)
    maximumIdx = numberList.index(maximum)
    
    print(maximum)

    print(maximumIdx + 1)

# __main()__
main()