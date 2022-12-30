def inputTwoInteger():
    a, b = map(int, input().split())

    return a, b

def createNumberList(n):
    numberList = []

    for i in range(1, n + 1):
        numberList.append(i)
    
    return numberList

def josephus(k, numberList):
    josephusList = []

    count = 1
    index = 0

    while(len(numberList) > 0):
        if(count == k):
            data = numberList[index]
            josephusList.append(data)

            del numberList[index]

            index -= 1

            count = 1
        
        else:
            count += 1
        
        index += 1
        
        if(index >= len(numberList)):
            index = 0

    return josephusList
            

def printList(josephusList):
    print("<", end = '')

    for i in josephusList:
        if(i == josephusList[len(josephusList) - 1]):
            print("%d>" % i, end = "")
        
        else:
            print("%d, " % i, end = "")
            
    print("")

def main():
    n, k = inputTwoInteger()
    numberList = createNumberList(n)
    josephusList = josephus(k, numberList)
    printList(josephusList)

# __main()__
main()