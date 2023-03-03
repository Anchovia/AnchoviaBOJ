import sys

def main():
    numberList = list()
    
    n = int(input())

    for i in range(n):
        number = int(sys.stdin.readline())
        numberList.append(number)

    numberList.sort(reverse=True)

    for j in numberList:
        print(j)

# __main__
main()