def inputTwoInteger():
    a, b = map(int, input().split())

    return a, b

def calculatedivisor(data):
    rawDivisorList = []

    for i in range(1, data + 1):
        if(data % i == 0):
            rawDivisorList.append(i)
    
    return rawDivisorList

def findGreatestCommonFactor(divisorList):
    dataList = divisorList[0]
    dataList.reverse()

    for i in dataList:
        if(i in divisorList[1]):

            return i

def findLowestCommonMultiple(a, b):
    data1 = a
    data2 = b

    while(data1 != data2):
        if(data1 < data2):
            data1 += a
        
        else:
            data2 += b
    
    return data1

def main():
    divisorList = []

    a, b = inputTwoInteger()

    rawDivisorList = calculatedivisor(a)
    divisorList.append(rawDivisorList)

    rawDivisorList = calculatedivisor(b)
    divisorList.append(rawDivisorList)

    print(findGreatestCommonFactor(divisorList))
    print(findLowestCommonMultiple(a, b))

# __main__
main()