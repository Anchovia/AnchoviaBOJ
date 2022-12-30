import sys

def searchLength(x, y):
    length = y - x

    if(length == 1):
        return 1
    
    elif(length == 2):
        return 2
    
    else:
        result = 2

        leftLength = length - 2

        i = 1

        while True:
            if(leftLength < 1):
                break

        return result


def main():
    resultList = []

    case = int(sys.stdin.readline().rstrip())

    for i in range(0, case):
        x, y = map(int, sys.stdin.readline().rstrip())

        result = searchLength(x, y)
        resultList.append(result)

    for j in resultList:
        print(j)