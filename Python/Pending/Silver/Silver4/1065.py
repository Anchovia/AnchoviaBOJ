import sys

def findHanNumber(n):
    result = 0

    for i in range(100, n + 1, 1):
        nowNumber = str(i)

        if(int(nowNumber[0]) < int(nowNumber[1])):
            a = int(nowNumber[2]) - int(nowNumber[1])

            if(int(nowNumber[1]) - a == int(nowNumber[0])):
                result += 1
        
        elif(int(nowNumber[0] > nowNumber[1])):
            a = int(nowNumber[0]) - int(nowNumber[1])

            if(int(nowNumber[1]) - a == int(nowNumber[2])):
                result += 1
        
        else:
            if(int(nowNumber[1]) == int(nowNumber[2])):
                result += 1

    return result

def main():
    n = int(sys.stdin.readline())

    if(n < 100):
        result = n
    
    elif(n < 1000):
        result = findHanNumber(n)

        result += 99
    
    else:
        result = findHanNumber(999)

        result += 99

    print(result)

# __main__
main()