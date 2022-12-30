import sys

def calculatedivisor(data):
    count = 0

    for i in range(1, data + 1):
        if(data % i == 0):
            count += 1
    
    if(count == 2):
        return True
    
    else:
        return False

def main():
    divisorList = []
    sum = 0
    
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    for num in range(m, n + 1):
        if(calculatedivisor(num) == True):
            divisorList.append(num)
        
        else:
            pass

    if(len(divisorList) == 0):
        print(-1)
    
    else:
        for i in divisorList:
            sum += i

        print(sum)
        print(divisorList[0])

# __main__
main()