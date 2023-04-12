def sumOfList(dataList):
    sum = 0

    for i in dataList:
        sum += i

    return sum

def main():
    kookList = list(map(int, input().split()))
    seaList = list(map(int, input().split()))

    kookSum = sumOfList(kookList)
    seaSum = sumOfList(seaList)

    if kookSum > seaSum:
        print(kookSum)
    
    elif kookSum == seaSum:
        print(kookSum)
    
    else:
        print(seaSum)

main()