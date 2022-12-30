import sys

def singleIntegerInput():
    n = int(sys.stdin.readline().rstrip())

    return n

def dataInput():
    data = list(sys.stdin.readline().rstrip())

    return data

def judgementVPS(stringData):
    index = 0

    while(index < len(stringData)):
        nowWord = stringData[index]

        try:
            futureWord = stringData[index + 1]
        
        except IndexError:
            return 'NO'

        if(nowWord == '('):
            if(futureWord == ')'):
                del stringData[index]
                del stringData[index]

                if(len(stringData) == 0):
                    return 'YES'
                
                index = 0
            
            else:
                if(')' not in stringData):
                    return 'NO'
                
                else:
                    index += 1
        
        else:
            return 'NO'
    
    return 'YES'

def printList(l):
    for i in l:
        print(i)

def main():
    resultList = []

    running = singleIntegerInput()

    for i in range(0, running):
        stringData = dataInput()
        result = judgementVPS(stringData)
        resultList.appen6d(result)

    printList(resultList)

# __main__
main()