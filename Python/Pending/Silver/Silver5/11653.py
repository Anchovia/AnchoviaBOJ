import sys

def singleIntegerInput():
    n = int(sys.stdin.readline())

    return n

def calculatedivisor(data):
    rawDivisorList = []

    for i in range(1, data + 1):
        if(data % i == 0):
            rawDivisorList.append(i)
    
    return rawDivisorList

def findIndex(divisorList):
    length = len(divisorList)

    if(length % 2 == 1):
        middleIndex = int(length / 2)
    
    else:
        middleIndex = int(length / 2 - 1)

    return middleIndex

def findPrimeFactorization(divisorList, middleIndex, n):
    resultList = []

    for i in range(1, middleIndex + 2):
        nowNumber = divisorList[i]

        while(n % nowNumber == 0):
            n /= nowNumber
            resultList.append(nowNumber)
    
    return resultList

def printList(l):
    for i in l:
        print(i)

def main():
    n = singleIntegerInput()
    if(n == 1):
        pass
    
    else:
        divisorList = calculatedivisor(n)

        middleIndex = findIndex(divisorList)

        resultList = findPrimeFactorization(divisorList, middleIndex, n)

        printList(resultList)

# __main__
main()