import sys

def main():
    numList = []
    result = 0

    data = sys.stdin.readline().rstrip()

    for i in data:
        numList.append(i)
    
    numList.sort(reverse=True)

    carry = len(numList)

    for j in numList:
        result += int(j) * 10 ** carry / 10
        carry -= 1
    
    print(int(result))

main()