import sys

def singleIntegerInput():
    n = int(sys.stdin.readline().rstrip())

    return n

def printList(l):
    for i in l:
        print(i)

def main():
    resultList = []

    n = singleIntegerInput()

    for i in range(0, n):
        num = singleIntegerInput()

        resultList.append(num)
    
    resultList.sort()
    
    printList(resultList)

# __main__
main()