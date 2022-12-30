import sys

def printFibo(n):
    fiboResult = []

    for i in range(0, n + 1):
        if(i == 0):
            fiboResult.append(0)
            
        elif(i == 1):
            fiboResult.append(1)
            
        
        else:
            result = fiboResult[i - 1] + fiboResult[i - 2]
            fiboResult.append(result)
    
    zeroResult = fiboResult[n - 1]
    oneResult = fiboResult[n]

    if(n == 0):
        zeroResult = 1

    print(zeroResult, oneResult)

def main():
    t = int(sys.stdin.readline().rstrip())

    for i in range(0, t):
        n = int(sys.stdin.readline().rstrip())

        printFibo(n)

# __main__
main()