import sys

def singleIntegerInput():
    n = int(sys.stdin.readline())

    return n

def listIntegerInput():
    l = list(map(int, sys.stdin.readline().split()))

    return l

def calculatedivisor(data):
    count = 0

    for i in range(1, data + 1):
        if(data % i == 0):
            count += 1
    
    if(count == 2):
        return True
    
    else:
        return False

def printList(l):
    for i in l:
        print(i)

def main():
    count = 0

    n = singleIntegerInput()

    dataList = listIntegerInput()

    for num in dataList:
        if(calculatedivisor(num) == True):
            count += 1
        
        else:
            pass

    print(count)

# __main__
main()